import sys
import os
import re
import csv, time

# import pandas as pd
import numpy as np
from subprocess import call
fips = '055'

# file and header
outfile = open(sys.argv[1][:-4]+'.csv','w')
outfile.write('pct16,candidate,total\n')


# loop through docs
for prop in range(53,68):

    call(['pdftotext','-layout',str(prop)+'.pdf'])
    pages = []
    currentPage = ''
    pageNo = 0


    with open(str(prop)+'.pdf'.replace('pdf','txt')) as file:
        # extract every other page (because of write in candidates)
        raw = file.read()
        pages = raw.split('')

        # loop through pages
        prop = ''
        for page in pages:
            # # look for candidate versus write in page
            # pagetype = ''
            # if 'HILLARY CLINTON' in page:
            #   # print 'MAIN CANDIDATE PAGE'
            #   pagetype = 'main'
            # elif 'MCMULLIN' in page:
            #   # print 'write-in page'
            #   pagetype = 'writein'
            # elif 'KAMALA' in page:
            #   pagetype = 'senate'
            # elif 'Yes' in page:
            #   pagetype = 'prop'
            # else:
            #   pagetype = "null"

            lines = page.split('\n')
            for line in lines:

                if 'PROPOSITION' in line:
                    pindex = line.index('PROPOSITION')
                    propnum = line[pindex+12:pindex+14]


                if line[:6].isdigit():
                    precinct = line[:6]
                    pct = precinct

                    line = line.replace(',','')

                    numbers = [int(s) for s in line.split() if s.isdigit()]
                    print numbers

                    yesvotes = str(numbers[-2])
                    novotes = str(numbers[-1])

                    outfile.write(fips+'-'+pct+',prop'+propnum+'_yes,'+yesvotes+'\n')
                    outfile.write(fips+'-'+pct+',prop'+propnum+'_no,'+novotes+'\n')
                # # look for proposition
                # if 'PROPOSITION' in line:
                #   prop = 'prop' + line[12:14]

                # # look for precinct number, which is five 
                # precinct = line[:7].strip()
                # if precinct.isdigit():
                #   # for when that first bit is a number
                #   print precinct

                #   lineindex = lines.index(line)
                #   totalline = lines[lineindex+4].replace(',','')
                #   numbers = [int(s) for s in totalline.split() if s.isdigit()]

                #   print numbers
                #   if pagetype == 'main':
                #       outfile.write('029-'+precinct+',pres_clinton,'+str(numbers[1])+'\n')
                #       outfile.write('029-'+precinct+',pres_trump,'+str(numbers[3])+'\n')
                #       outfile.write('029-'+precinct+',pres_johnson,'+str(numbers[4])+'\n')
                #       outfile.write('029-'+precinct+',pres_stein,'+str(numbers[0])+'\n')
                #       outfile.write('029-'+precinct+',pres_lariva,'+str(numbers[2])+'\n')
                #   elif pagetype == 'writein':
                #       outfile.write('029-'+precinct+',pres_other,'+str(numbers[0])+'\n')
                #   elif pagetype == 'senate':
                #       outfile.write('029-'+precinct+',ussenate_harris,'+str(numbers[1])+'\n')
                #       outfile.write('029-'+precinct+',ussenate_sanchez,'+str(numbers[0])+'\n')
                #   elif pagetype == 'prop':
                #       outfile.write('029-'+precinct+','+prop+'_yes,'+str(numbers[0])+'\n')
                #       outfile.write('029-'+precinct+','+prop+'_no,'+str(numbers[1])+'\n')
                #   # print lines[lineindex+4]

outfile.close()