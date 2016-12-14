import requests, time, json, urllib

f = open('props.csv','w')
f.write('pct16,race,yes,no\n')


for contest in range(6,23):
    print contest
    url = 'https://gis.nevcounty.net/arcgis/rest/services/web_public/ElectionResults201611/MapServer/'+str(contest)+'/query?where=1%3D1&text=&objectIds=&time=&geometry=&geometryType=esriGeometryEnvelope&inSR=&spatialRel=esriSpatialRelIntersects&relationParam=&outFields=*&returnGeometry=false&maxAllowableOffset=&geometryPrecision=&outSR=&returnIdsOnly=false&returnCountOnly=false&orderByFields=&groupByFieldsForStatistics=&outStatistics=&returnZ=false&returnM=false&gdbVersion=&returnDistinctValues=false&returnTrueCurves=false&resultOffset=&resultRecordCount=&f=pjson'

    result = json.load(urllib.urlopen(url))

    # r = requests.get(url)
    # data = json.loads(r)
    precincts = result['features']

    for precinct in precincts:
        # print precinct
        pct16 = '057-'+precinct['attributes']['CONS_PREC']
        race = precinct['attributes']['ContestTitle']
        if precinct['attributes']['Candidate1'] == 'YES':
            yesvotes = precinct['attributes']['NumVotes1']
            novotes = precinct['attributes']['NumVotes2']
            f.write(str(pct16)+','+str(race)+','+str(yesvotes)+','+str(novotes)+'\n')
        else:
            print "PROBLEM"
        print race
    time.sleep(1)