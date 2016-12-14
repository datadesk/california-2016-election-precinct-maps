import json
import csv
import re
import os

if not os.path.exists('results/'):
    os.makedirs('results/')

myjson = open('ALL.json').read()
json2 = open('sum.json').read()

fullresults = json.loads(myjson)
sumresults = json.loads(json2)

precincts = fullresults['Contests']
races = sumresults['Contests']

# header = ['county_name','county','state','trump','clinton','johnson','stein','other']
# csvwriter.writerow(header)

count = 0
for p in range(len(precincts)):
	for c in range(len(precincts[p]['C'])):
		race_name = "unknown"
		for r in range(len(races)):
			if races[r]['K'] == precincts[p]['C'][c]:
				race_name = races[r]['C']
				# print race_name
				has_headers = True
				header_row = ['pct16']
				for h in range(len(races[r]['CH'])):
					header_row.append(races[r]['CH'][h])
				output = open('results/%s.csv' % re.sub(r'\W','',race_name),'w')
				csvwriter = csv.writer(output)
				csvwriter.writerow(header_row)

			if race_name == "unknown":
				# print "NO RACE HEADER"
				output = open('results/%s.csv' % precincts[p]['C'][c],'w')
				csvwriter = csv.writer(output)
				has_headers = False
				race_name = precincts[p]['C'][c]
			output.close()

for p in range(len(precincts)):
	print precincts[p]['A']
	for c in range(len(precincts[p]['C'])):
		race_name = "unknown"
		for r in range(len(races)):
			if races[r]['K'] == precincts[p]['C'][c]:
				race_name = races[r]['C']
				output = open('results/%s.csv' % re.sub(r'\W','',race_name),'a+')
				csvwriter = csv.writer(output)

			if race_name == "unknown":
				# print "NO RACE HEADER"
				output = open('results/%s.csv' % precincts[p]['C'][c],'a+')
				csvwriter = csv.writer(output)
				has_headers = False
				race_name = precincts[p]['C'][c]


		precinct_name = '089-%s' % (re.sub(r'\W','',precincts[p]['A']))
		precinct_results = [precinct_name]
		for y in range(len(precincts[p]['V'][c])):
			precinct_results.append(precincts[p]['V'][c][y])
		csvwriter.writerow(precinct_results)
		output.close()