# we need to "import" these libraries to scrape
from bs4 import BeautifulSoup
import time, urllib

# this is the three-digit code for the county of Calaveras
fips = '009'

# open the file we'll write to
# the 'w' means write. There's also read 'r' and append 'a'
outfile = open('results.csv','w')

# write header line
outfile.write('pct16,candidate,total\n')

# loop through the precincts available which starts at 1 and ends at 29
for x in range(1,30):
    # this checks the number of digits because there's a leading zero in the URL
    if len(str(x)) == 1:
        # prepends a zero if it's a single digit
        precinct = '0'+str(x)
    else:
        # otherwise it's fine as is
        precinct = str(x)

    # here's the URL we want to use with the precinct subbed in on the fly
    url = 'http://elections.calaverasgov.us/Portals/clerk/Docs/Elections/Results/PREC00'+ precinct +'.HTM'

    # open the url
    page = urllib.urlopen(url)

    # parse the url's information into searchable HTML via BeautifulSoup library
    soup = BeautifulSoup(page, 'html.parser')

    # look for the <pre> tag and pull the text out
    text = soup.find('pre').text

    # split that text into lines
    lines = text.split('\n')

    # store the line's index for later use, starting at zero
    lineindex = 0

    # loop through those lines
    for line in lines:
        # print line
        # look for precinct number
        if '00'+precinct in line:
            pct = line[15:18] # this is where the three-digit precinct number is, which differs from above
            print pct

        # check if line is the presidential race
        if 'PRESIDENT AND VICE PRESIDENT' in line:
            # go two lines down and grab characters number 55-61
            johnson = lines[lineindex+2][55:61].strip() # strip removes leading and ending whitespace
            # etc for each candidate
            stein = lines[lineindex+3][55:61].strip()
            clinton = lines[lineindex+4][55:61].strip()
            lariva = lines[lineindex+5][55:61].strip()
            trump = lines[lineindex+6][55:61].strip()
            other = lines[lineindex+7][55:61].strip()

            outfile.write(fips+'-'+pct+',pres_clinton,'+clinton+'\n')
            outfile.write(fips+'-'+pct+',pres_trump,'+trump+'\n')
            outfile.write(fips+'-'+pct+',pres_stein,'+stein+'\n')
            outfile.write(fips+'-'+pct+',pres_lariva,'+lariva+'\n')
            outfile.write(fips+'-'+pct+',pres_johnson,'+johnson+'\n')
            outfile.write(fips+'-'+pct+',pres_other,'+other+'\n')

        # else if this text is in the line
        elif 'UNITED STATES SENATOR' in line:
            sanchez = lines[lineindex+2][55:61].strip()
            harris = lines[lineindex+3][55:61].strip()

            outfile.write(fips+'-'+pct+',ussenate_harris,'+harris+'\n')
            outfile.write(fips+'-'+pct+',ussenate_sanchez,'+sanchez+'\n')

        elif 'PROPOSITION' in line:
            propindex = line.index('PROPOSITION')
            propnum = line[propindex+12:propindex+14]

            yesvotes = lines[lineindex+2][55:61].strip()
            novotes = lines[lineindex+3][55:61].strip()

            outfile.write(fips+'-'+pct+',prop'+propnum+'_yes,'+yesvotes+'\n')
            outfile.write(fips+'-'+pct+',prop'+propnum+'_no,'+novotes+'\n')



            # if pagetype == 'main':
            #     outfile.write(fips+'-'+precinct+',pres_clinton,'+str(numbers[4])+'\n')
            #     outfile.write(fips+'-'+precinct+',pres_trump,'+str(numbers[6])+'\n')
            #     outfile.write(fips+'-'+precinct+',pres_stein,'+str(numbers[3])+'\n')
            #     outfile.write(fips+'-'+precinct+',pres_lariva,'+str(numbers[5])+'\n')
            #     outfile.write(fips+'-'+precinct+',pres_johnson,'+str(numbers[7])+'\n')
            # elif pagetype == 'writein':
            #     outfile.write(fips+'-'+precinct+',pres_other,'+str(numbers[1])+'\n')
            # elif pagetype == 'senate':
            #     outfile.write(fips+'-'+precinct+',ussenate_harris,'+str(numbers[4])+'\n')
            #     outfile.write(fips+'-'+precinct+',ussenate_sanchez,'+str(numbers[3])+'\n')
            # elif pagetype == 'prop':
            #     outfile.write(fips+'-'+precinct+','+prop+'_yes,'+str(numbers[3])+'\n')
            #     outfile.write(fips+'-'+precinct+','+prop+'_no,'+str(numbers[4])+'\n')


        lineindex = lineindex + 1 # increase the line after handling line

    # this waits one second before going to the next page
    time.sleep(1)
