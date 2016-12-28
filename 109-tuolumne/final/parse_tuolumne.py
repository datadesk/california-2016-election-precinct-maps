import time

file = open("final-results.txt","r")
lines = file.readlines()

outfile = open('results.csv','w')
outfile.write('pct16,candidate,total\n')

fips = '011'

lineindex = 0
for line in lines:
    # print line.replace('\n','')

    # find precinct number
    if line[:2] == '00':
        precinctnum = line[:4]
        precinctname = line[5:]

        pct = precinctname

    if 'PRESIDENT AND VICE PRESIDENT' in line:
        stein = lines[lineindex+3][46:51].strip()
        clinton = lines[lineindex+4][46:51].strip()
        lariva = lines[lineindex+5][46:51].strip()
        trump = lines[lineindex+6][46:51].strip()
        johnson = lines[lineindex+2][46:51].strip()
        other = lines[lineindex+7][46:51].strip()

        outfile.write(fips+'-'+pct+',pres_clinton,'+clinton+'\n')
        outfile.write(fips+'-'+pct+',pres_trump,'+trump+'\n')
        outfile.write(fips+'-'+pct+',pres_stein,'+stein+'\n')
        outfile.write(fips+'-'+pct+',pres_lariva,'+lariva+'\n')
        outfile.write(fips+'-'+pct+',pres_johnson,'+johnson+'\n')
        outfile.write(fips+'-'+pct+',pres_other,'+other+'\n')

    elif 'UNITED STATES SENATOR' in line:
        sanchez = lines[lineindex+2][46:51].strip()
        harris = lines[lineindex+3][46:51].strip()

        outfile.write(fips+'-'+pct+',ussenate_harris,'+harris+'\n')
        outfile.write(fips+'-'+pct+',ussenate_sanchez,'+sanchez+'\n')

    elif 'PROPOSITION' in line:
        propnum = line[12:14]

        yesvotes = lines[lineindex+2][46:51].strip()
        novotes = lines[lineindex+3][46:51].strip()

        outfile.write(fips+'-'+pct+',prop'+propnum+'_yes,'+yesvotes+'\n')
        outfile.write(fips+'-'+pct+',prop'+propnum+'_no,'+novotes+'\n')


    lineindex = lineindex + 1

outfile.close()