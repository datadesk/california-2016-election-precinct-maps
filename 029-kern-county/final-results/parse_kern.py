import sys
import os
import re
import csv, time

# import pandas as pd
import numpy as np
from subprocess import call
fips = '065'

call(['pdftotext','-layout',sys.argv[1]])
pages = []
currentPage = ''
pageNo = 0
if not os.path.exists('results/'):
    os.makedirs('results/')

precinctre = re.compile("[.\n](\d{5})")

with open(sys.argv[1].replace('pdf','txt')) as file:
	# extract every other page (because of write in candidates)
	raw = file.read()
	pages = raw.split('')

	# loop through pages
	for page in pages:
		# look for candidate versus write in page
		if 'HILLARY CLINTON' in page:
			print 'MAIN CANDIDATE PAGE'
		elif 'EVAN MCMULLIN' in page:
			print 'write-in page'

		lines = page.split('\n')
		for line in lines:
			# look for precinct number, which is five 
			precinct = line[:7].strip()
			if precinct.isdigit():
				# for when that first bit is a number
				print precinct

				lineindex = lines.index(line)
				totalline = lineindex+4
				print[int(s) for s in lines[totalline].split() if s.isdigit()]
				# print lines[lineindex+4]


			# result = precinctre.search(line)
			# print result
		# print page
		time.sleep(1)


	# filename = 'results/%s.csv' % sys.argv[1].replace('.pdf','')
	# out = open(filename,'w') # open out file
	# header row
	# out.write('pct16,total,voters,count,votes,%s_yes,yespct,%s_no,nopct\n' % (sys.argv[1].replace('.pdf',''),sys.argv[1].replace('.pdf','')))

	# if "Precinct                           Precinct" in line

	# resultstring = re.sub(r'(.*\n){12}( *(Jurisdiction|Total|Polling|VBM|\d{7})?)',r'\2',file.read(),flags=re.MULTILINE)
	# resultstring = re.sub(r'(?:\n\s{3,})(Total.+)',r'\n\1',resultstring,flags=re.MULTILINE)
	# # resultstring = re.sub(r'(?:\n\s{3,})(\w{3} \d{3}-\d{2}|MB\d{2})',r'\n\1',resultstring,flags=re.MULTILINE)
	# print resultstring
	# results = [re.findall(r'(?: *)(\d{7})(?:(\n)(.*\n){2,3} *)(Total.+)',resultstring,flags=re.MULTILINE)]
	# # print results
	# for x in range(0,len(results[0])):
	# 	out.write('%s,%s\n' % (results[0][x][0],re.sub(r' +',',',''.join(results[0][x][len(results[0][x])-1]))))



# with open(sys.argv[1].replace('pdf','txt')) as file:
# 	filename = 'results/%s.csv' % sys.argv[1].replace('.pdf','')
# 	out = open(filename,'w')
# 	out.write('pct16,total,voters,count,votes,%s_yes,yespct,%s_no,nopct\n' % (sys.argv[1].replace('.pdf',''),sys.argv[1].replace('.pdf','')))
# 	resultstring = re.sub(r'(.*\n){12}( *(Jurisdiction|Total|Polling|VBM|\d{7})?)',r'\2',file.read(),flags=re.MULTILINE)
# 	resultstring = re.sub(r'(?:\n\s{3,})(Total.+)',r'\n\1',resultstring,flags=re.MULTILINE)
# 	# resultstring = re.sub(r'(?:\n\s{3,})(\w{3} \d{3}-\d{2}|MB\d{2})',r'\n\1',resultstring,flags=re.MULTILINE)
# 	print resultstring
# 	results = [re.findall(r'(?: *)(\d{7})(?:(\n)(.*\n){2,3} *)(Total.+)',resultstring,flags=re.MULTILINE)]
# 	# print results
# 	for x in range(0,len(results[0])):
# 		out.write('%s,%s\n' % (results[0][x][0],re.sub(r' +',',',''.join(results[0][x][len(results[0][x])-1]))))