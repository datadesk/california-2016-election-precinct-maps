import sys
import os
import re
import csv, time

# import pandas as pd
import numpy as np
from subprocess import call
fips = '091'



# file and header
outfile = open('results.csv','w')
outfile.write('pct16,candidate,total\n')


# loop through all pdfs
for filename in os.listdir('pdfs/'):

	call(['pdftotext','-layout',filename])
	pages = []
	currentPage = ''
	pageNo = 0

	with open(sys.argv[1].replace('pdf','txt')) as file:
		# extract every other page (because of write in candidates)
		raw = file.read()
		pages = raw.split('')

		# loop through pages
		prop = ''
		for page in pages:

			# # look for candidate versus write in page
			# pagetype = ''
			# if 'HILLARY CLINTON' in page:
			# 	# print 'MAIN CANDIDATE PAGE'
			# 	pagetype = 'main'
			# elif 'EVAN MCMULLIN' in page:
			# 	# print 'write-in page'
			# 	pagetype = 'writein'
			# elif 'KAMALA' in page:
			# 	pagetype = 'senate'
			# elif 'Yes' in page:
			# 	pagetype = 'prop'
			# else:
			# 	pagetype = "null"

			lines = page.split('\n')
			for line in lines:
				lineindex = lines.index(line)

				# store precinct from argument
				precinct = sys.argv[1][:-4]

				# split page in two
				leftside = line[:60]
				rightside = line[61:]

				if 'President and Vice President' in leftside:
					race = 'pres'
					stein = [int(s) for s in lines[lineindex+8][:60].split() if s.isdigit()][0]
					clinton = [int(s) for s in lines[lineindex+9][:60].split() if s.isdigit()][0]
					lariva = [int(s) for s in lines[lineindex+10][:60].split() if s.isdigit()][0]
					trump = [int(s) for s in lines[lineindex+11][:60].split() if s.isdigit()][0]
					johnson = [int(s) for s in lines[lineindex+12][:60].split() if s.isdigit()][0]
					writein = [int(s) for s in lines[lineindex+13][:60].split() if s.isdigit()][0]

					outfile.write(precinct+',pres_clinton,'+str(clinton)+'\n')
					outfile.write(precinct+',pres_trump,'+str(trump)+'\n')
					outfile.write(precinct+',pres_johnson,'+str(johnson)+'\n')
					outfile.write(precinct+',pres_stein,'+str(stein)+'\n')
					outfile.write(precinct+',pres_lariva,'+str(lariva)+'\n')
					outfile.write(precinct+',pres_other,'+str(writein)+'\n')

				# for props	
				elif 'PROPOSITION' in leftside:
					propnum = leftside[12:14]

					yesvotes = [int(s) for s in lines[lineindex+8][:60].split() if s.isdigit()][0]
					novotes = [int(s) for s in lines[lineindex+9][:60].split() if s.isdigit()][0]

					outfile.write(precinct+',prop'+propnum+'yes,'+str(yesvotes)+'\n')
					outfile.write(precinct+',prop'+propnum+'no,'+str(novotes)+'\n')

				elif 'PROPOSITION' in rightside:
					propnum = rightside[-2:]

					yesvotes = [int(s) for s in lines[lineindex+8][:60].split() if s.isdigit()][0]
					novotes = [int(s) for s in lines[lineindex+9][:60].split() if s.isdigit()][0]

					outfile.write(precinct+',prop'+propnum+'yes,'+str(yesvotes)+'\n')
					outfile.write(precinct+',prop'+propnum+'no,'+str(novotes)+'\n')

				elif 'US Senator' in leftside:
					sanchez = [int(s) for s in lines[lineindex+8][:60].split() if s.isdigit()][0]
					harris = [int(s) for s in lines[lineindex+9][:60].split() if s.isdigit()][0]

					outfile.write(precinct+',ussenate_harris,'+str(harris)+'\n')
					outfile.write(precinct+',ussenate_sanchez,'+str(sanchez)+'\n')

outfile.close()