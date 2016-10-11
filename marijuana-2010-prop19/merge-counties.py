#!/usr/bin/python
import ogr, sys, time

drv = ogr.GetDriverByName('ESRI Shapefile') #We will load a shape file
ds_in = drv.Open("c003_g10_sov_data_by_g10_srprec.dbf")    #Get the contents of the shape file
lyr_in = ds_in.GetLayer(0)    #Get the shape file's first layer

#Put the title of the field you are interested in here
psupp = lyr_in.GetLayerDefn().GetFieldIndex("SRPREC")

print lyr_in

for feat_in in lyr_in:
    print feat_in.GetFieldAsString(psupp)

#If the latitude/longitude we're going to use is not in the projection
#of the shapefile, then we will get erroneous results.
#The following assumes that the latitude longitude is in WGS84
#This is identified by the number "4326", as in "EPSG:4326"
#We will create a transformation between this and the shapefile's
#project, whatever it may be
# geo_ref = lyr_in.GetSpatialRef()
# point_ref=ogr.osr.SpatialReference()
# point_ref.ImportFromEPSG(4326)
# ctran=ogr.osr.CoordinateTransformation(point_ref,geo_ref)



# # open points file
# j = open("parcel-points.csv","r")
# points = j.readlines()

# # open output file
# f = open("outpoint-6.csv","a")


# def check(lat, lon, line, ain, percent):

#     #Transform incoming longitude/latitude to the shapefile's projection
#     [lon,lat,z]=ctran.TransformPoint(lon,lat)

#     #Create a point
#     pt = ogr.Geometry(ogr.wkbPoint)
#     pt.SetPoint_2D(0, lon, lat)

#     #Set up a spatial filter such that the only features we see when we
#     #loop through "lyr_in" are those which overlap the point defined above
#     lyr_in.SetSpatialFilter(pt)

#     #Loop through the overlapped features and display the field of interest
#     for feat_in in lyr_in:
#         # f.write(line + ',' feat_in.GetFieldAsString(idx_reg) + '\n')
#         # print ain, lon, lat, feat_in.GetFieldAsString(idx_reg)
#         f.write(str(ain) + ',' + str(lon) + ',' + str(lat) + ',' + feat_in.GetFieldAsString(idx_reg) + '\n')


# # loop through points
# for point in points[2362694:]:
#     feats = point.split(',')
#     line = point.replace('\n','')
#     ain = feats[0]
#     index = points.index(point)
#     percent = float(index)/float(len(points))

#     if len(feats[1]) > 0 and len(feats[2]) > 0:
#         check(float(feats[1]),float(feats[2]),line,ain,percent)
#         sys.stdout.write("Download progress: %d%%   \r" % (percent*100) + str(index) )
#         sys.stdout.flush()

# f.close()
