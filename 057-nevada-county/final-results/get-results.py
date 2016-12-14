import requests, time, json, urllib

for contest in range(9,10):
    print contest
    url = 'https://gis.nevcounty.net/arcgis/rest/services/web_public/ElectionResults201611/MapServer/'+str(contest)+'/query?where=1%3D1&text=&objectIds=&time=&geometry=&geometryType=esriGeometryEnvelope&inSR=&spatialRel=esriSpatialRelIntersects&relationParam=&outFields=*&returnGeometry=false&maxAllowableOffset=&geometryPrecision=&outSR=&returnIdsOnly=false&returnCountOnly=false&orderByFields=&groupByFieldsForStatistics=&outStatistics=&returnZ=false&returnM=false&gdbVersion=&returnDistinctValues=false&returnTrueCurves=false&resultOffset=&resultRecordCount=&f=pjson'

    result = json.load(urllib.urlopen(url))

    # r = requests.get(url)
    # data = json.loads(r)
    precincts = result['features']

    for precinct in precincts:
        print precinct
        pct16 = precinct['attributes']['CONS_PREC']
        print pct16
        time.sleep(1)