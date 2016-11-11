import json
import csv
import re

myjson = open('details.json').read()
json2 = open('sum.json').read()
fullresults = json.loads(myjson)
sumresults = json.loads(json2)
races = fullresults['Contests']
headers = sumresults['Contests']

# header = ['county_name','county','state','trump','clinton','johnson','stein','other']
# csvwriter.writerow(header)

count = 0
for r in range(len(races)):

	if races[r]['K'] == headers[r]['K']:
		race_name = headers[r]['C']
		has_headers = True
		header_row = ['pct16']
		for c in range(len(headers[r]['CH'])):
			header_row.append(headers[r]['CH'][c])
		output = open('results/%s.csv' % re.sub(r'\W','',race_name),'w')
		csvwriter = csv.writer(output)
		csvwriter.writerow(header_row)

	else:
		print "NO RACE HEADER"
		output = open('results/%s.csv' % races[r]['K'],'w')
		csvwriter = csv.writer(output)
		has_headers = False
		race_name = races[r]['K']

	for x in range(len(races[r]['P'])):
		precinct_results = [races[r]['P'][x]]
		for y in range(len(races[r]['V'][x])):
			precinct_results.append(races[r]['V'][x][y])
		csvwriter.writerow(precinct_results)
	output.close()