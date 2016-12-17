import sys
import os
import re
import csv, time

# import pandas as pd
import numpy as np
from subprocess import call
fips = '093'

call(['pdftotext','-layout',sys.argv[1]])
pages = []
currentPage = ''
pageNo = 0

precinctre = re.compile("[.\n](\d{5})") # a pinch of regex to find precinct number

# file and header
outfile = open(sys.argv[1][:-4]+'.csv','w')
outfile.write('pct16,candidate,total\n')


with open(sys.argv[1].replace('pdf','txt')) as file:
	# extract every other page (because of write in candidates)
	raw = file.read()
	pages = raw.split('')

	# loop through pages
	prop = ''
	for page in pages:
		# look for candidate versus write in page
		pagetype = ''
		if 'HILLARY CLINTON' in page:
			# print 'MAIN CANDIDATE PAGE'
			pagetype = 'main'
		elif 'Evan McMullin' in page:
			# print 'write-in page'
			pagetype = 'writein'
		elif 'KAMALA' in page:
			pagetype = 'senate'
		elif 'Yes' in page:
			pagetype = 'prop'
		else:
			pagetype = "null"

		linecount = 0
		lines = page.split('\n')
		for line in lines:
			lineindex = linecount

			# look for proposition
			if 'PROPOSITION' in line:
				prop = 'prop' + line[12:14]

			# find the precinct
			if 'Election Day' in line:

				precinct = lines[lineindex-1][:30].strip()

				print precinct

				totalline = lines[lineindex+2].replace(',','')
				numbers = [int(s) for s in totalline.split() if s.isdigit()]
				# print numbers

				if pagetype == 'main':
					outfile.write(fips+precinct+',pres_clinton,'+str(numbers[4])+'\n')
					outfile.write(fips+precinct+',pres_trump,'+str(numbers[6])+'\n')
					outfile.write(fips+precinct+',pres_stein,'+str(numbers[3])+'\n')
					outfile.write(fips+precinct+',pres_lariva,'+str(numbers[5])+'\n')
				elif pagetype == 'writein':
					outfile.write(fips+precinct+',pres_johnson,'+str(numbers[0])+'\n')
					outfile.write(fips+precinct+',pres_other,'+str(numbers[1])+'\n')
				elif pagetype == 'senate':
					outfile.write(fips+precinct+',ussenate_harris,'+str(numbers[4])+'\n')
					outfile.write(fips+precinct+',ussenate_sanchez,'+str(numbers[3])+'\n')
				elif pagetype == 'prop':
					outfile.write(fips+precinct+','+prop+'_yes,'+str(numbers[3])+'\n')
					outfile.write(fips+precinct+','+prop+'_no,'+str(numbers[4])+'\n')
				# print lines[lineindex+4]
			linecount = linecount + 1

outfile.close()