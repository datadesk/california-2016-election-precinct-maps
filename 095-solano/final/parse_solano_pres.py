import sys
import os
import re
import csv

filepath = sys.argv[1]
if not os.path.exists('results/'):
    os.makedirs('results/')


f = open(filepath,'r')
precincts = f.read().split('\n\n')
headers = ['pct16','pres_clinton','pres_trump','pres_johnson','pres_stein','pres_lariva','pres_other']
output = open('results/%s.csv' % filepath.replace('.txt',''),'w')
csvwriter = csv.writer(output)
csvwriter.writerow(headers)

for precinct in precincts:
    # print precincts
    row = []
    pct16 = re.search(r'(?:Precinct\n.+)(\d{5})',precinct,flags=re.MULTILINE).group(1)
    row.append("095-%s" % pct16)

    clintonline = re.search(r'.*CLINTON .+',precinct).group(0)
    # print yesline
    clinton = re.split(r'\t',clintonline)[1]
    row.append(clinton)

    trumpline = re.search(r'.*TRUMP .+',precinct).group(0)
    # print trumpline
    trump = re.split(r'\t',trumpline)[1]
    row.append(trump)

    johnsonline = re.search(r'.*JOHNSON .+',precinct).group(0)
    # print johnsonline
    johnson = re.split(r'\t',johnsonline)[1]
    row.append(johnson)

    steinline = re.search(r'.*STEIN .+',precinct).group(0)
    # print steinline
    stein = re.split(r'\t',steinline)[1]
    row.append(stein)

    larivaline = re.search(r'.*LA RIVA .+',precinct).group(0)
    # print larivaline
    lariva = re.split(r'\t',larivaline)[1]
    row.append(lariva)

    otherline = re.search(r'.*WRITE-IN .+',precinct).group(0)
    # print otherline
    other = re.split(r'\t',otherline)[1]
    row.append(other)    


    csvwriter.writerow(row)

f.close()
output.close()