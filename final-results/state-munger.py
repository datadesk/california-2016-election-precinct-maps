# This script will calculate other fields needed for precinct-results

from __future__ import division
import sys, time, csv, os
# from osgeo import ogr

# should be the 3-digit FIPS and county name
file = "california-2016-county-results"

inithdrs = ['countyfp10','pres_clinton','pres_trump','pres_johnson','pres_stein','pres_lariva','pres_other','ussenate_harris','ussenate_sanchez','prop51_yes','prop51_no','prop52_yes','prop52_no','prop53_yes','prop53_no','prop54_yes','prop54_no','prop55_yes','prop55_no','prop56_yes','prop56_no','prop57_yes','prop57_no','prop58_yes','prop58_no','prop59_yes','prop59_no','prop60_yes','prop60_no','prop61_yes','prop61_no','prop62_yes','prop62_no','prop63_yes','prop63_no','prop64_yes','prop64_no','prop65_yes','prop65_no','prop66_yes','prop66_no','prop67_yes','prop67_no']

addedhdrs = ['pres_clinton_per','pres_trump_per','pres_third_per','pres_winner','pres_margin','prop51_yes_per','prop51_no_per','prop52_yes_per','prop52_no_per','prop53_yes_per','prop53_no_per','prop54_yes_per','prop54_no_per','prop55_yes_per','prop55_no_per','prop56_yes_per','prop56_no_per','prop57_yes_per','prop57_no_per','prop58_yes_per','prop58_no_per','prop59_yes_per','prop59_no_per','prop60_yes_per','prop60_no_per','prop61_yes_per','prop61_no_per','prop62_yes_per','prop62_no_per','prop63_yes_per','prop63_no_per','prop64_yes_per','prop64_no_per','prop65_yes_per','prop65_no_per','prop66_yes_per','prop66_no_per','prop67_yes_per','prop67_no_per']



with open(file+'.csv','r') as csvinput:
    with open(file+'-munged.csv', 'w') as csvoutput:
        writer = csv.writer(csvoutput, lineterminator='\n')
        reader = csv.reader(csvinput,delimiter=',')


        all = []
        row = next(reader)

        # check that input file is formatted right
        if (row == inithdrs):

            # add new columns
            row = row + addedhdrs
            all.append(row)

            for row in reader:
                # convert numbers to floats
                for i in range(1,len(row)):
                    row[i] = float(row[i])

                # add new data fields
                # pres_clinton_per = 'test'
                if (sum(row[1:7]) == 0):
                    pres_clinton_per = 0
                    pres_trump_per = 0
                    pres_third_per = 0
                    pres_winner = "none"
                    pres_margin = 0
                else:
                    pres_clinton_per = round(row[1]/sum(row[1:7])*100,2)
                    pres_trump_per = round(row[2]/sum(row[1:7])*100,2)
                    pres_third_per = round(sum(row[3:7])/sum(row[1:7])*100,2)
                    # find winner
                    if row[1] == max(row[1:7]):
                        pres_winner = "clinton"
                    elif row[2] == max(row[1:7]):
                        pres_winner = "trump"
                    elif row[3] == max(row[1:7]):
                        pres_winner = "johnson"
                    elif row[4] == max(row[1:7]):
                        pres_winner = "stein"
                    elif row[5] == max(row[1:7]):
                        pres_winner = "other"
                    else:
                        pres_winner = "none"

                    # figure out winner's margin
                    canidates = row[1:7]
                    canidates.sort(reverse=True) # sort desc
                    pres_margin = round((canidates[0]/sum(canidates) - canidates[1]/sum(canidates))*100,2)

                # temp values
                votedensity = 0

                # get precinct's vote desnity from matching shapefile and total pres vote
                # shapefile = "../ready-precincts/"+file+".shp"
                # driver = ogr.GetDriverByName("ESRI Shapefile")
                # dataSource = driver.Open(shapefile, 0)

                # layer = dataSource.GetLayer()

                # for feature in layer:
                # #     print row[0]
                #     # print feature.GetField("pct16")
                #     if row[0] == feature.GetField("pct16"):
                #         miles = feature.GetField("area") * 0.000000386102159
                #         votedensity = sum(row[1:7])/miles


                newvals = [pres_clinton_per, pres_trump_per, pres_third_per, pres_winner, pres_margin]

                # script out prop row values
                for x in range(5,38,2):
                    valName = addedhdrs[x-2]
                    x1 = x # first val
                    x2 = x+1 # second val
                    if (row[x1]+row[x2]) == 0:
                        value1 = 0
                        value2 = 0
                    else:
                        value1 = round(row[x1]/(row[x1]+row[x2])*100,2)
                        value2 = round(row[x2]/(row[x1]+row[x2])*100,2)
                    newvals = newvals + [value1,value2]

                # add these values to the row
                row = row + newvals

                # row.append(pres_clinton_per)
                all.append(row)

            writer.writerows(all)

        else:
            # WARNING
            print "WARNING: Your columns are not formatted correctly. https://github.com/datadesk/california-2016-election-precinct-maps/blob/master/README.md#data-format"