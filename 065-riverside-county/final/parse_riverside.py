import sys
import os
import re
import csv
import pandas as pd
import numpy as np
from subprocess import call
fips = '065'

call(['pdftotext','-layout',sys.argv[1]])
pages = []
currentPage = ''
pageNo = 0
if not os.path.exists('results/'):
    os.makedirs('results/')

with open(sys.argv[1].replace('pdf','txt')) as file:
	filename = '%s.csv' % sys.argv[1].replace('.pdf','')
	out = open(filename,'w')
	csvwriter = csv.writer(out)
	resultstring = re.sub(r'(.*\n)+?(\d{5} )',r'\2',file.read(),flags=re.MULTILINE)
	resultstring = re.sub(r' +Turnout \(%\)\n +',',',resultstring,flags=re.MULTILINE)
	resultstring = re.sub(r'\*+| +Insufficient\n +| +Turnout\s+| +to +Protect |Voter +Privacy\n +| +\*+ *','  ',resultstring,flags=re.MULTILINE)
	resultstring = re.sub(r' {2,}(?!\n)',',',resultstring,flags=re.MULTILINE)
	resultstring = re.sub(r'(\n\d{5})( .+?,)',r'\1,',resultstring)
	results = resultstring.split('\n')

	# the first 36ish lines are no good, let's cut them out (THIS CAN CHANGE PER COUNTY)
	final_results = results[68:-6];
	

	# column_names = ['pct16','reg','ballots','turnout','pres_stein','pres_clinton','pres_lariva','pres_trump','pres_johnson','ussen_sanchez','ussen_harris']
	# column_names = ['pct16','reg','ballots','turnout','prop51_yes','prop51_no','prop52_yes','prop52_no','prop53_yes','prop53_no','prop54_yes','prop54_no']
	# column_names = ['pct16','reg','ballots','turnout','prop55_yes','prop55_no','prop56_yes','prop56_no','prop57_yes','prop57_no','prop58_yes','prop58_no']
	# column_names = ['pct16','reg','ballots','turnout','prop59_yes','prop59_no','prop60_yes','prop60_no','prop61_yes','prop61_no','prop62_yes','prop62_no']
	column_names = ['pct16','reg','ballots','turnout','prop63_yes','prop63_no','prop64_yes','prop64_no','prop65_yes','prop65_no','prop66_yes','prop66_no']
	# column_names = ['pct16','reg','ballots','turnout','prop67_yes','prop67_no']
	csvwriter.writerow(column_names)
	# print final_results[2191]
	results_array = []
	for row in final_results:
		row_array = row.split(',')[0:len(column_names)]
		row_array[0] = '%s-%s' % (fips,row_array[0])
		results_array.append(row_array)
		csvwriter.writerow(row_array)
	out.close()

	# out.write('pct16,reg,ballots,turnout,pres_stein,pres_clinton,pres_lariva,pres_trump,pres_johnson,ussen_sanchez,ussen_harris,?\n')
	# column_types = [agate.Text(),agate.Number(),agate.Number(),agate.Number(),agate.Number(),agate.Number(),agate.Number(),agate.Number(),agate.Number(),agate.Number(),agate.Number()]
	# result_table = agate.Table.from_csv(results_array,column_names,column_types)
	# result_table.to_csv('results/agate_output.csv')
	
	result_table = pd.read_csv(filename,dtype={'pct16':str})
	by_pct = result_table.groupby(['pct16']).sum()
	by_pct.to_csv('results/%s-results.csv' % sys.argv[1].replace('.pdf',''))

	# print resultstring
	# results = [re.findall(r'(?: *)(\d{7})(?:(\n)(.*\n){2,3} *)(Total.+)',resultstring,flags=re.MULTILINE)]
	
	# for x in range(0,len(results[0])):
	# 	out.write('%s,%s\n' % (results[0][x][0],re.sub(r' +',',',''.join(results[0][x][len(results[0][x])-1]))))