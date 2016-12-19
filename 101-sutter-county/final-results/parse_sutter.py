import sys
import os
import re
import csv
import pandas as pd
import numpy as np
from subprocess import call
fips = '101'

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
	# remove the top of each page (some number of lines after the )
	resultstring = re.sub(r'(Vote-By-Mail Ballot Totals ?|All-Mail-Ballot Totals ?)\n? *(\d+)',r'\1   \2','%s' % file.read(),flags=re.MULTILINE)
	resultstring = re.sub(r'()(.*\n)+?(.+? \d{4} |.+? Vote-By-Mail Ballot Totals +|.+? All-Mail-Ballot Totals +)',r'\3',resultstring,flags=re.MULTILINE)
	# remove the bottom with precinct totals
	resultstring = re.sub(r'(\n\nPrecinct Totals)(.*\n)+',r'',resultstring,flags=re.MULTILINE)
	print resultstring

	# resultstring = re.sub(r' +Turnout \(%\)\n +',',',resultstring,flags=re.MULTILINE)

	# remove insufficient turnout line, while keeping numbers scattered through it
	# resultstring = re.sub(r'\*+|\s+Insufficient\n +|\n +| +Turnout\s+| +to +Protect |Voter +Privacy\n +| +\*+ *','  ',resultstring,flags=re.MULTILINE)
	
	# replace multiple spaces with a comma
	resultstring = re.sub(r' {2,}(?!\n)',',',resultstring,flags=re.MULTILINE)

	# put number and name in separate columns
	resultstring = re.sub(r'(.+? )(\d{4},|- .+?,)',r'\1,\2',resultstring)
	results = resultstring.split('\n')

	# cut off the last leftover line
	final_results = results[0:-1];
	

	# column_names = ['pct16','pctnum','reg','ballots','turnout','pres_stein','pres_clinton','pres_lariva','pres_trump','pres_johnson','ussenate_sanchez','ussenate_harris']
	# column_names = ['pct16','pctnum','reg','ballots','turnout','prop51_yes','prop51_no','prop52_yes','prop52_no','prop53_yes','prop53_no','prop54_yes','prop54_no']
	# column_names = ['pct16','pctnum','reg','ballots','turnout','prop55_yes','prop55_no','prop56_yes','prop56_no','prop57_yes','prop57_no','prop58_yes','prop58_no']
	# column_names = ['pct16','pctnum','reg','ballots','turnout','prop59_yes','prop59_no','prop60_yes','prop60_no','prop61_yes','prop61_no','prop62_yes','prop62_no']
	# column_names = ['pct16','pctnum','reg','ballots','turnout','prop63_yes','prop63_no','prop64_yes','prop64_no','prop65_yes','prop65_no','prop66_yes','prop66_no']
	column_names = ['pct16','pctnum','reg','ballots','turnout','prop67_yes','prop67_no']
	csvwriter.writerow(column_names)
	# print final_results[2191]
	results_array = []
	for row in final_results:
		row_array = row.split(',')[0:len(column_names)]
		row_array[1] = '%s-%s' % (fips,row_array[1])
		results_array.append(row_array)
		csvwriter.writerow(row_array)
	out.close()

	# out.write('pct16,reg,ballots,turnout,pres_stein,pres_clinton,pres_lariva,pres_trump,pres_johnson,ussen_sanchez,ussen_harris,?\n')
	# column_types = [agate.Text(),agate.Number(),agate.Number(),agate.Number(),agate.Number(),agate.Number(),agate.Number(),agate.Number(),agate.Number(),agate.Number(),agate.Number()]
	# result_table = agate.Table.from_csv(results_array,column_names,column_types)
	# result_table.to_csv('results/agate_output.csv')
	
	result_table = pd.read_csv(filename,dtype={'pct16':str})
	by_pct = result_table.groupby(['pct16']).agg({
			# 'pctnum':'max','reg':'min','ballots':'min','turnout':'min','pres_stein':'sum','pres_clinton':'sum','pres_lariva':'sum','pres_trump':'sum','pres_johnson':'sum','ussenate_sanchez':'sum','ussenate_harris':'sum'
			# 'pctnum':'max','reg':'min','ballots':'min','turnout':'min','prop51_yes':'sum','prop51_no':'sum','prop52_yes':'sum','prop52_no':'sum','prop53_yes':'sum','prop53_no':'sum','prop54_yes':'sum','prop54_no':'sum'
			# 'pctnum':'max','reg':'min','ballots':'min','turnout':'min','prop55_yes':'sum','prop55_no':'sum','prop56_yes':'sum','prop56_no':'sum','prop57_yes':'sum','prop57_no':'sum','prop58_yes':'sum','prop58_no':'sum'
			# 'pctnum':'max','reg':'min','ballots':'min','turnout':'min','prop59_yes':'sum','prop59_no':'sum','prop60_yes':'sum','prop60_no':'sum','prop61_yes':'sum','prop61_no':'sum','prop62_yes':'sum','prop62_no':'sum'
			# 'pctnum':'max','reg':'min','ballots':'min','turnout':'min','prop63_yes':'sum','prop63_no':'sum','prop64_yes':'sum','prop64_no':'sum','prop65_yes':'sum','prop65_no':'sum','prop66_yes':'sum','prop66_no':'sum'
			'pctnum':'max','reg':'min','ballots':'min','turnout':'min','prop67_yes':'sum','prop67_no':'sum'
		})
	by_pct[column_names[1:2] + column_names[5:]].to_csv('results/%s-results.csv' % sys.argv[1].replace('.pdf',''))

	# print resultstring
	# results = [re.findall(r'(?: *)(\d{7})(?:(\n)(.*\n){2,3} *)(Total.+)',resultstring,flags=re.MULTILINE)]
	
	# for x in range(0,len(results[0])):
	# 	out.write('%s,%s\n' % (results[0][x][0],re.sub(r' +',',',''.join(results[0][x][len(results[0][x])-1]))))