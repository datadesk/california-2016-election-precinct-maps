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
	# out.write('pct16,total,voters,count,votes,pres_stein,stein_pct,pres_clinton,clinton_pct,pres_lariva,lariva_pct\n')
	# out.write('pct16,total,pres_trump,trump_pct,pres_johnson,johnson_pct,pres_kotlikoff,kotlikoff_pct,pres_maturen,maturen_pct,pres_mcmullin,mcmullin_pct,pres_sanders,sanders_pct\n')
	# out.write('pct16,total,pres_white,white_pct,write_in,write_in_pct\n')
	# out.write('pct16,total,voters,count,votes,ussenate_harris,harris_pct,ussenate_sanchez,sanchez_pct\n')
	out.write('pct16,total,voters,count,votes,%s_yes,yespct,%s_no,nopct\n' % (sys.argv[1].replace('.pdf',''),sys.argv[1].replace('.pdf','')))
	resultstring = re.sub(r'(.*\n){13}( *(Jurisdiction|Total|Polling|VBM (ABS)|CP\d+|MB\d+)?)',r'\2','%s' % file.read(),flags=re.MULTILINE)
	resultstring = re.sub(r'(?:\n\s{3,})(Total.+|Polling.+)',r'\n\1',resultstring,flags=re.MULTILINE)
	# resultstring = re.sub(r'(?:\n\s{3,})(\w{3} \d{3}-\d{2}|MB\d{2})',r'\n\1',resultstring,flags=re.MULTILINE)
	print resultstring
	results = [re.findall(r'(?: *)(CP\d+|MB\d+) ([\d \-,]+)(?:\n(.*\n){2,3} *)(Total.+)',resultstring,flags=re.MULTILINE)]
	# print results
	for x in range(0,len(results[0])):
		out.write('%s,%s\n' % (results[0][x][0],re.sub(r' +',',',''.join(results[0][x][len(results[0][x])-1]))))