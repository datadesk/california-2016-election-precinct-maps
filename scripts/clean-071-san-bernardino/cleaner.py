import time

#open file
f = open("Report_EDATE20161108_PrecinctReport_20161109.txt","r")
lines = f.readlines()

#write file
j = open("071-san-bernardino.csv",'w')

# header row
j.write('pct16,pres_clinton,pres_trump,pres_johnson,pres_stein,pres_lariva,pres_other,ussenate_harris,ussenate_sanchez,prop51_yes,prop51_no,prop52_yes,prop52_no,prop53_yes,prop53_no,prop54_yes,prop54_no,prop55_yes,prop55_no,prop56_yes,prop56_no,prop57_yes,prop57_no,prop58_yes,prop58_no,prop59_yes,prop59_no,prop60_yes,prop60_no,prop61_yes,prop61_no,prop62_yes,prop62_no,prop63_yes,prop63_no,prop64_yes,prop64_no,prop65_yes,prop65_no,prop66_yes,prop66_no,prop67_yes,prop67_no\n')

precincts = {}

pctlist = []
# create list of precincts
for line in lines[1:]:
    cell = line.split('\t')
    pctname = cell[0]
    if pctname not in pctlist:
        pctlist.append(pctname)
    candidate = cell[1]
    contest = cell[8]
    totalvote = cell[9]

    if contest+candidate == 'State Proposition 59NO':
        hdr = "prop59_no"
    elif contest+candidate == 'State Proposition 59YES':
        hdr = "prop59_yes"
    elif contest+candidate == 'State Proposition 58NO':
        hdr = "prop58_no"
    elif contest+candidate == 'State Proposition 58YES':
        hdr = "prop58_yes"
    elif contest+candidate == 'State Proposition 57NO':
        hdr = "prop57_no"
    elif contest+candidate == 'State Proposition 57YES':
        hdr = "prop57_yes"
    elif contest+candidate == 'State Proposition 56NO':
        hdr = "prop56_no"
    elif contest+candidate == 'State Proposition 56YES':
        hdr = "prop56_yes"
    elif contest+candidate == 'State Proposition 55NO':
        hdr = "prop55_no"
    elif contest+candidate == 'State Proposition 55YES':
        hdr = "prop55_yes"
    elif contest+candidate == 'State Proposition 54NO':
        hdr = "prop54_no"
    elif contest+candidate == 'State Proposition 54YES':
        hdr = "prop54_yes"
    elif contest+candidate == 'State Proposition 53NO':
        hdr = "prop53_no"
    elif contest+candidate == 'State Proposition 53YES':
        hdr = "prop53_yes"
    elif contest+candidate == 'State Proposition 52NO':
        hdr = "prop52_no"
    elif contest+candidate == 'State Proposition 52YES':
        hdr = "prop52_yes"
    elif contest+candidate == 'State Proposition 51NO':
        hdr = "prop51_no"
    elif contest+candidate == 'State Proposition 51YES':
        hdr = "prop51_yes"
    elif contest+candidate == 'United States SenatorDEM - LORETTA L. SANCHEZ':
        hdr = "ussenate_sanchez"
    elif contest+candidate == 'United States SenatorDEM - KAMALA D. HARRIS':
        hdr = "ussenate_harris"
    elif contest+candidate == 'President and Vice PresidentPF - GLORIA ESTELA LA RIVA AND DENNIS J. BANKS':
        hdr = "pres_lariva"
    elif contest+candidate == 'President and Vice PresidentGRN - JILL STEIN AND AJAMU BARAKA':
        hdr = "pres_stein"
    elif contest+candidate == 'President and Vice PresidentLIB - GARY JOHNSON AND BILL WELD':
        hdr = "pres_johnson"
    elif contest+candidate == 'President and Vice PresidentRAI - DONALD J. TRUMP AND MICHAEL R. PENCE':
        hdr = "pres_trump"
    elif contest+candidate == 'President and Vice PresidentDEM - HILLARY CLINTON AND TIM KAINE':
        hdr = "pres_clinton"
    elif contest+candidate == 'State Proposition 64YES':
        hdr = "prop64_yes"
    elif contest+candidate == 'State Proposition 63NO':
        hdr = "prop63_no"
    elif contest+candidate == 'State Proposition 63YES':
        hdr = "prop63_yes"
    elif contest+candidate == 'State Proposition 62NO':
        hdr = "prop62_no"
    elif contest+candidate == 'State Proposition 62YES':
        hdr = "prop62_yes"
    elif contest+candidate == 'State Proposition 61NO':
        hdr = "prop61_no"
    elif contest+candidate == 'State Proposition 61YES':
        hdr = "prop61_yes"
    elif contest+candidate == 'State Proposition 60NO':
        hdr = "prop60_no"
    elif contest+candidate == 'State Proposition 60YES':
        hdr = "prop60_yes"
    elif contest+candidate == 'State Proposition 64NO':
        hdr = "prop64_no"
    elif contest+candidate == 'State Proposition 65YES':
        hdr = "prop65_yes"
    elif contest+candidate == 'State Proposition 65NO':
        hdr = "prop65_no"
    elif contest+candidate == 'State Proposition 66YES':
        hdr = "prop66_yes"
    elif contest+candidate == 'State Proposition 66NO':
        hdr = "prop66_no"
    elif contest+candidate == 'State Proposition 67YES':
        hdr = "prop67_yes"
    elif contest+candidate == 'State Proposition 67NO':
        hdr = "prop67_no"
    else:
        hdr = "null"


    # check and see if its in there
    if pctname not in precincts:
        precincts[pctname] = {}
    else:
        precincts[pctname][hdr] = totalvote


for pct in pctlist:
    # print precincts[pct]['pres_clinton']
    # time.sleep(1)
    j.write('071-'+pct+','+precincts[pct]["pres_clinton"]+','+precincts[pct]["pres_trump"]+','+precincts[pct]["pres_johnson"]+','+precincts[pct]["pres_stein"]+','+precincts[pct]["pres_lariva"]+',0,'+precincts[pct]["ussenate_harris"]+','+precincts[pct]["ussenate_sanchez"]+','+precincts[pct]["prop51_yes"]+','+precincts[pct]["prop51_no"]+','+precincts[pct]["prop52_yes"]+','+precincts[pct]["prop52_no"]+','+precincts[pct]["prop53_yes"]+','+precincts[pct]["prop53_no"]+','+precincts[pct]["prop54_yes"]+','+precincts[pct]["prop54_no"]+','+precincts[pct]["prop55_yes"]+','+precincts[pct]["prop55_no"]+','+precincts[pct]["prop56_yes"]+','+precincts[pct]["prop56_no"]+','+precincts[pct]["prop57_yes"]+','+precincts[pct]["prop57_no"]+','+precincts[pct]["prop58_yes"]+','+precincts[pct]["prop58_no"]+','+precincts[pct]["prop59_yes"]+','+precincts[pct]["prop59_no"]+','+precincts[pct]["prop60_yes"]+','+precincts[pct]["prop60_no"]+','+precincts[pct]["prop61_yes"]+','+precincts[pct]["prop61_no"]+','+precincts[pct]["prop62_yes"]+','+precincts[pct]["prop62_no"]+','+precincts[pct]["prop63_yes"]+','+precincts[pct]["prop63_no"]+','+precincts[pct]["prop64_yes"]+','+precincts[pct]["prop64_no"]+','+precincts[pct]["prop65_yes"]+','+precincts[pct]["prop65_no"]+','+precincts[pct]["prop66_yes"]+','+precincts[pct]["prop66_no"]+','+precincts[pct]["prop67_yes"]+','+precincts[pct]["prop67_no"]+'\n')



# print precincts


# print precincts

# # roll through them lines
# for line in lines[1:]:
#     cell = line.split('\t')
#     print cell[0]

#     precinct = cell[1]
#     contest = cell[0]

    # time.sleep(1)