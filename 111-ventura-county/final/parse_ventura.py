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
		print race_name
		has_headers = True
		header_row = ['pct16']
		for c in range(len(headers[r]['CH'])):
			raceheaders = re.sub(r'[^\x00-\x7F]+','X', headers[r]['CH'][c])
			header_row.append(raceheaders)
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
		# print re.search(r'(?:- )(.+\d+.*)(?=[AFLSR]*$)',races[r]['P'][x],flags=re.MULTILINE).group(0)
		# precinct_results = ['111-%s' % re.search(r'(?:- )(.+\d+.*)(?=[AFLSR]*$)',races[r]['P'][x]).group(0)]
		# precinct_results = re.sub(r'- |- MB ','',precinct_results)
		precinct_results = re.search(r'(?:- )(.+\d+D*\d*)(?=[AFLSR]*$)',races[r]['P'][x]).group(0)
		precinct_results = ['111-%s' % re.sub(r'- (MB )*','',precinct_results).replace(' ','-').replace('#','NO').replace('/','-')]
		for y in range(len(races[r]['V'][x])):
			precinct_results.append(races[r]['V'][x][y])
		csvwriter.writerow(precinct_results)
	output.close()