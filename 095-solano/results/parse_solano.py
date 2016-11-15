import time

files = ['prop52']

allData = {}
precincts = []

for file in files:
    print file
    f = open(file+'.txt','r')
    lines = f.read().split('\n')
    # j = open(file+'-cleaned.txt','w')

    # headers for new file
    # j.write("precinct,"+file+"_yes,"+file+"_no\n")

    linelen = len(lines)

    for line in range(0,linelen,6):
        precinct = lines[line+1]

        if precinct not in precincts:
            precincts.append(precinct)
            allData[precinct] = {}

        # check if prop in the file
        if file not in allData[precinct]:
            if " YES " in lines[line+3]:
                yesvotes = lines[line+3].split('\t')[1]
                novotes = lines[line+4].split('\t')[1]
                allData[precinct][file] = {'yes':yesvotes,'no':novotes}
            elif " NO " in lines[line+3]:
                yesvotes = lines[line+4].split('\t')[1]
                novotes = lines[line+3].split('\t')[1]
                allData[precinct][file] = {'yes':yesvotes,'no':novotes}
    f.close()

print allData

        # print lines[line+1]

    # # newline = "" # starting string for lines once they're constructed
    # for line in lines:

    #     cells = line.split('\t')

    #     if "Precinct" in line:
    #         index = lines.index(line)
    #         precinct = lines[lines.index(line)+1]
    #         # newline += precinct + ','
    #         print index

    #         if precinct not in precincts:
    #             precincts.append(precinct)
    #             allData[precinct] = {}

    #     # elif " YES " in line:
    #     #     # newline += cells[1] + ','

    #     # elif " NO " in line:
    #         # newline += cells[1] + '\n'

    #     # elif len(line) == 0:
    #         # j.write(newline)
    #         # newline = ""
    # j.close()
    # print allData

    #     # print line
    #     # time.sleep(1)