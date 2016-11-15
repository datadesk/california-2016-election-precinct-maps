import time

files = ['prop51']

allData = {}
precincts = []

for file in files:
    f = open(file+'.txt','r').read()
    j = open(file+'-cleaned.txt','w')

    # headers for new file
    j.write("precinct,"+file+"_yes,"+file+"_no\n")

    lines = f.split('\n')
    # newline = "" # starting string for lines once they're constructed
    for line in lines:
        cells = line.split('\t')

        if "Precinct" in line:
            # newline = ""
            precinct = lines[lines.index(line)+1]
            # newline += precinct + ','

            if precinct not in precincts:
                precincts.append(precinct)
                allData[precinct] = {}

        elif " YES " in line:
            # newline += cells[1] + ','

        elif " NO " in line:
            # newline += cells[1] + '\n'

        elif len(line) == 0:
            # j.write(newline)
            # newline = ""
    j.close()

        # print line
        # time.sleep(1)