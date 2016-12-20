import sys
import os
import re
from subprocess import call
call(['pdftotext','-layout',sys.argv[1]])
pages = []
currentPage = ''
pageNo = 0
if not os.path.exists('results/'):
    os.makedirs('results/')

with open(sys.argv[1].replace('pdf','txt')) as file:
	for line in file:
		if re.match(r'()',line):
			pages.append(currentPage)
			pageNo += 1
			print "page %s" % (pageNo)
			currentPage = line
		else:
			currentPage += line
	file.close()

# precincts = [re.findall(r'((?<= - )\d{7}[^,]+)',line) for line in file]
currentRace = ''
out = None
for page in pages:
	race = re.findall(r'(?:COUNTY OF LOS ANGELES.+\n\n)(.+\n)',page,flags=re.MULTILINE);
	raceString = ''
	if race:
		raceString = re.sub(r' {2,}',' ',race[0]);
	else:
		raceScring = currentRace
	if currentRace != raceString:
		if out != None:
			out.close()
		filename = 'results/%s.csv' % (raceString.replace(' ',''))
		out = open(filename,'w')
		currentRace = raceString;
		# if race:
		# 	out.write('RACE: %s' % (currentRace))
		# else:
		# 	print "no match"

	results = [re.findall(r'((?<= - )\d{7}[^ ]+)(?:.+\n)(?:.+\n)(?:TOTAL)(.+\n)',page,flags=re.MULTILINE)]
	for x in range(0,len(results[0])):
		out.write(re.sub(r' {2,}',',',''.join(results[0][x])))