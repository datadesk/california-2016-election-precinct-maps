import time

#open file
f = open("20161108_UnOfficial_EN_cv.txt","r")

lines = f.readlines()

#write file
j = open("073-san-diego-precincts.csv",'w')

# header row
# j.write('pct16,pres_clinton,pres_johnson,pres_stein,pres_lariva,pres_other,ussenate_harris,ussenate_sanchez,prop51_yes,prop51_no,prop52_yes,prop52_no,prop53_yes,prop53_no,prop54_yes,prop54_no,prop55_yes,prop55_no,prop56_yes,prop56_no,prop57_yes,prop57_no,prop58_yes,prop58_no,prop59_yes,prop59_no,prop60_yes,prop60_no,prop61_yes,prop61_no,prop62_yes,prop62_no,prop63_yes,prop63_no,prop64_yes,prop64_no,prop65_yes,prop65_no,prop66_yes,prop66_no,prop67_yes,prop67_no\n')

precincts = {}

pcts = []

for line in lines[1:]:
    cell = line.split('\t')
    pctname = cell[2].replace('"','')
    cid = cell[3].replace('"','')

    if pctname not in precincts:
        precincts[pctname] = cid
        pcts.append(pctname)

print precincts

for pct in pcts:
    j.write(precincts[pct]+','+pct+'\n')

j.close()

# pctlist = []

# # create list of precincts
# for line in lines[1:]:

#     cell = line.split('\t')

#     total = cell[10].replace('"','')



#     if total == "Total":
#         pctname = cell[2].replace('"','')
#         if pctname not in pctlist:
#             pctlist.append(pctname)

#         candidate = cell[6].replace('"','')
#         contest = cell[4].replace('"','')

#         if '\r\n' in cell[11]:
#             totalvote = cell[11].replace('"','').replace('\r\n','')
#         else:

#         if contest+candidate == 'PROP 59 - STATE                       LEGISLATIVE ADVISORY QUESTIONNO':
#             hdr = "prop59_no"
#         elif contest+candidate == 'PROP 59 - STATE                       LEGISLATIVE ADVISORY QUESTIONYES':
#             hdr = "prop59_yes"
#         elif contest+candidate == 'PROP 58 - STATE                       ENGLISH PROFICIENCYNO':
#             hdr = "prop58_no"
#         elif contest+candidate == 'PROP 58 - STATE                       ENGLISH PROFICIENCYYES':
#             hdr = "prop58_yes"
#         elif contest+candidate == 'PROP 57 - STATE                       CRIMINAL SENTENCESNO':
#             hdr = "prop57_no"
#         elif contest+candidate == 'PROP 57 - STATE                       CRIMINAL SENTENCESYES':
#             hdr = "prop57_yes"
#         elif contest+candidate == 'PROP 56 - STATE                       CIGARETTE TAXNO':
#             hdr = "prop56_no"
#         elif contest+candidate == 'PROP 56 - STATE                       CIGARETTE TAXYES':
#             hdr = "prop56_yes"
#         elif contest+candidate == 'PROP 55 - STATE                       TAX EXTENSIONNO':
#             hdr = "prop55_no"
#         elif contest+candidate == 'PROP 55 - STATE                       TAX EXTENSIONYES':
#             hdr = "prop55_yes"
#         elif contest+candidate == 'PROP 54 - STATE                       LEGISLATURENO':
#             hdr = "prop54_no"
#         elif contest+candidate == 'PROP 54 - STATE                       LEGISLATUREYES':
#             hdr = "prop54_yes"
#         elif contest+candidate == 'PROP 53 - STATE                       REVENUE BONDSNO':
#             hdr = "prop53_no"
#         elif contest+candidate == 'PROP 53 - STATE                       REVENUE BONDSYES':
#             hdr = "prop53_yes"
#         elif contest+candidate == 'PROP 52 - STATE                       MEDI-CAL HOSPITAL FEENO':
#             hdr = "prop52_no"
#         elif contest+candidate == 'PROP 52 - STATE                       MEDI-CAL HOSPITAL FEEYES':
#             hdr = "prop52_yes"
#         elif contest+candidate == 'PROP 51 - STATE                       SCHOOL BONDSNO':
#             hdr = "prop51_no"
#         elif contest+candidate == 'PROP 51 - STATE                       SCHOOL BONDSYES':
#             hdr = "prop51_yes"
#         elif contest+candidate == 'UNITED STATES SENATORLORETTA L. SANCHEZ':
#             hdr = "ussenate_sanchez"
#         elif contest+candidate == 'UNITED STATES SENATORKAMALA D. HARRIS':
#             hdr = "ussenate_harris"
#         elif contest+candidate == 'PRESIDENT/VICE PRESIDENTLA RIVA/BANKS':
#             hdr = "pres_lariva"
#         elif contest+candidate == 'PRESIDENT/VICE PRESIDENTSTEIN/BARAKA':
#             hdr = "pres_stein"
#         elif contest+candidate == 'PRESIDENT/VICE PRESIDENTJOHNSON/WELD':
#             hdr = "pres_johnson"
#         elif contest+candidate == 'PRESIDENT/VICE PRESIDENTTRUMP/PENCE':
#             hdr = "pres_trump"
#         elif contest+candidate == 'PRESIDENT/VICE PRESIDENTCLINTON/KAINE':
#             hdr = "pres_clinton"
#         elif contest+candidate == 'PROP 64 - STATE                       MARIJUANA LEGALIZATIONYES':
#             hdr = "prop64_yes"
#         elif contest+candidate == 'PROP 63 - STATE                       FIREARMS, AMMUNITION SALESNO':
#             hdr = "prop63_no"
#         elif contest+candidate == 'PROP 63 - STATE                       FIREARMS, AMMUNITION SALESYES':
#             hdr = "prop63_yes"
#         elif contest+candidate == 'PROP 62 - STATE                       DEATH PENALTYNO':
#             hdr = "prop62_no"
#         elif contest+candidate == 'PROP 62 - STATE                       DEATH PENALTYYES':
#             hdr = "prop62_yes"
#         elif contest+candidate == 'PROP 61 - STATE                       PRESCRIPTION DRUG PURCHASESNO':
#             hdr = "prop61_no"
#         elif contest+candidate == 'PROP 61 - STATE                       PRESCRIPTION DRUG PURCHASESYES':
#             hdr = "prop61_yes"
#         elif contest+candidate == 'PROP 60 - STATE                       ADULT FILMSNO':
#             hdr = "prop60_no"
#         elif contest+candidate == 'PROP 60 - STATE                       ADULT FILMSYES':
#             hdr = "prop60_yes"
#         elif contest+candidate == 'PROP 64 - STATE                       MARIJUANA LEGALIZATIONNO':
#             hdr = "prop64_no"
#         elif contest+candidate == 'PROP 65 - STATE                       CARRYOUT BAGSYES':
#             hdr = "prop65_yes"
#         elif contest+candidate == 'PROP 65 - STATE                       CARRYOUT BAGSNO':
#             hdr = "prop65_no"
#         elif contest+candidate == 'PROP 66 - STATE                       DEATH PENALTYYES':
#             hdr = "prop66_yes"
#         elif contest+candidate == 'PROP 66 - STATE                       DEATH PENALTYNO':
#             hdr = "prop66_no"
#         elif contest+candidate == 'PROP 67 - STATE                           Ban on Single-Use Plastic BagsYES':
#             hdr = "prop67_yes"
#         elif contest+candidate == 'PROP 67 - STATE                           Ban on Single-Use Plastic BagsNO':
#             hdr = "prop67_no"
#         else:
#             hdr = "null"


#         # check and see if its in there
#         if pctname not in precincts:
#             precincts[pctname] = {}
#         else:
#             precincts[pctname][hdr] = totalvote

# # print precincts

# for pct in pctlist:
#     # print precincts[pct]['pres_clinton']
#     # time.sleep(1)
#     print pct
#     print precincts[pct]
#     j.write('071-'+pct+','+precincts[pct]["pres_clinton"]+','+precincts[pct]["pres_trump"]+','+precincts[pct]["pres_johnson"]+','+precincts[pct]["pres_stein"]+','+precincts[pct]["pres_lariva"]+',0,'+precincts[pct]["ussenate_harris"]+','+precincts[pct]["ussenate_sanchez"]+','+precincts[pct]["prop51_yes"]+','+precincts[pct]["prop51_no"]+','+precincts[pct]["prop52_yes"]+','+precincts[pct]["prop52_no"]+','+precincts[pct]["prop53_yes"]+','+precincts[pct]["prop53_no"]+','+precincts[pct]["prop54_yes"]+','+precincts[pct]["prop54_no"]+','+precincts[pct]["prop55_yes"]+','+precincts[pct]["prop55_no"]+','+precincts[pct]["prop56_yes"]+','+precincts[pct]["prop56_no"]+','+precincts[pct]["prop57_yes"]+','+precincts[pct]["prop57_no"]+','+precincts[pct]["prop58_yes"]+','+precincts[pct]["prop58_no"]+','+precincts[pct]["prop59_yes"]+','+precincts[pct]["prop59_no"]+','+precincts[pct]["prop60_yes"]+','+precincts[pct]["prop60_no"]+','+precincts[pct]["prop61_yes"]+','+precincts[pct]["prop61_no"]+','+precincts[pct]["prop62_yes"]+','+precincts[pct]["prop62_no"]+','+precincts[pct]["prop63_yes"]+','+precincts[pct]["prop63_no"]+','+precincts[pct]["prop64_yes"]+','+precincts[pct]["prop64_no"]+','+precincts[pct]["prop65_yes"]+','+precincts[pct]["prop65_no"]+','+precincts[pct]["prop66_yes"]+','+precincts[pct]["prop66_no"]+','+precincts[pct]["prop67_yes"]+','+precincts[pct]["prop67_no"]+'\n')


