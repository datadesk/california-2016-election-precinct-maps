import sys
import os
import re
from subprocess import call
fips = '077'

call(['pdftotext','-layout',sys.argv[1]])
pages = []
currentPage = ''
pageNo = 0
if not os.path.exists('results/'):
    os.makedirs('results/')

with open(sys.argv[1].replace('pdf','txt')) as file:
	filename = 'results/%s.csv' % sys.argv[1].replace('.pdf','')
	out = open(filename,'w')
	# out.write('pct16,total,voters,vote_for,count,votes,%s_yes,yespct,%s_no,nopct\n' % (sys.argv[1].replace('.pdf',''),sys.argv[1].replace('.pdf','')))
	out.write('pct16,total,voters,vote_for,count,votes,pres_stein,stein_pct,pres_clinton,clinton_pct,pres_lariva,lariva_pct,pres_trump,trump_pct\n')
	# out.write('pct16,total,pres_johnson,johnson_pct,pres_other,other_pct,voters,vote_for,count,votes,ussenate_sanchez,sanchez_pct,ussenate_harris,harris_pct\n')
	resultstring = re.sub(r'()(.*\n)+? *(Jurisdiction|Total|Polling|VBM|Early|Provisional|M\d{6}|\d{7}?)',r'\3','%s' % file.read(),flags=re.MULTILINE)
	# resultstring = re.sub(r'(?:\n\s{5,})(Total.+)',r'\n\1',resultstring,flags=re.MULTILINE)
	# resultstring = re.sub(r'(?:\n\s{3,})(\w{3} \d{3}-\d{2}|MB\d{2})',r'\n\1',resultstring,flags=re.MULTILINE)
	results = [re.findall(r' *(M\d{6}|\d{7})(?:(.*\n){2,}? *)(Total.+)',resultstring,flags=re.MULTILINE)]
	# print resultstring
	# print results
	for x in range(0,len(results[0])):
		out.write('%s-%s,%s\n' % (fips,results[0][x][0].replace('M','0'),re.sub(r' +',',',''.join(results[0][x][len(results[0][x])-1])).replace('-','0')))