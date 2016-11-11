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
	race = re.findall(r'(?:Santa Barbara County.+\n.+\n.+\n.+\n.+\n)(.+)',page,flags=re.MULTILINE);
	raceString = ''
	if race:
		raceString = re.sub(r' {2,}',' ',race[0]);
		print raceString
	else:
		raceScring = currentRace
	if currentRace != raceString:
		if out != None:
			out.close()
		filename = 'results/%s.csv' % (re.sub(r'\W','',raceString))
		out = open(filename,'w')
		currentRace = raceString;
		# if race:
		# 	out.write('RACE: %s' % (currentRace))
		# else:
		# 	print "no match"

	results = [re.findall(r'(\d{2}-\d{4})(?:(.*\n){3,}?)(?:  Total)(.+\n)',page,flags=re.MULTILINE)]
	print results
	for x in range(0,len(results[0])):
		out.write(re.sub(r' {2,}',',',''.join(results[0][x])))