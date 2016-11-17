import sys
import os
import re
import csv

filepath = sys.argv[1]
if not os.path.exists('results/'):
    os.makedirs('results/')


f = open(filepath,'r')
precincts = f.read().split('\n\n')
headers = ['pct16','%s_yes' % (filepath.replace('.txt','')),'%s_no' % (filepath.replace('.txt',''))]
output = open('results/%s.csv' % filepath.replace('.txt',''),'w')
csvwriter = csv.writer(output)
csvwriter.writerow(headers)

for precinct in precincts:
    # print precincts
    row = []
    pct16 = re.search(r'(?:Precinct\n.+)(\d{5})(?:\n)',precinct,flags=re.MULTILINE).group(1)
    row.append(pct16)

    yesline = re.search(r'.*YES .+',precinct).group(0)
    # print yesline
    yes = re.split(r'\t',yesline)[1]
    row.append(yes)

    noline = re.search(r'.*NO .+',precinct).group(0)
    # print noline
    no = re.split(r'\t',noline)[1]
    row.append(no)
    csvwriter.writerow(row)

f.close()
output.close()