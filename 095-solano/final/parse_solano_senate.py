import sys
import os
import re
import csv

filepath = sys.argv[1]
if not os.path.exists('results/'):
    os.makedirs('results/')


f = open(filepath,'r')
precincts = f.read().split('\n\n')
headers = ['pct16','sen_harris','sen_sanchez']
output = open('results/%s.csv' % filepath.replace('.txt',''),'w')
csvwriter = csv.writer(output)
csvwriter.writerow(headers)

for precinct in precincts:
    # print precincts
    row = []
    pct16 = re.search(r'(?:Precinct\n.+)(\d{5})',precinct,flags=re.MULTILINE).group(1)
    row.append("095-%s" % pct16)

    harrisline = re.search(r'.*HARRIS .+',precinct).group(0)
    # print yesline
    harris = re.split(r'\t',harrisline)[1]
    row.append(harris)

    sanchezline = re.search(r'.*SANCHEZ .+',precinct).group(0)
    # print sanchezline
    sanchez = re.split(r'\t',sanchezline)[1]
    row.append(sanchez)


    csvwriter.writerow(row)

f.close()
output.close()