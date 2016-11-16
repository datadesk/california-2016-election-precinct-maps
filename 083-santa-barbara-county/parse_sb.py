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
	filename = 'results/%s.csv' % sys.argv[1].replace('.pdf','')
	out = open(filename,'w')
	resultstring = re.sub(r'Santa Barbara County(.*\n){13}','',file.read(),flags=re.MULTILINE)
	# print resultstring
	results = [re.findall(r'(\d{2}-\d{4})(?:(.+\n){3})(.+)',resultstring,flags=re.MULTILINE)]
	# print results
	for x in range(0,len(results[0])):
		out.write('%s,%s\n' % (results[0][x][0],re.sub(r' +',',',''.join(results[0][x][len(results[0][x])-1]))))