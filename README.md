# California's most detailed election result map EVER

![calif-precincts](https://cloud.githubusercontent.com/assets/695934/21558065/5e417640-cde9-11e6-85d1-ebfa1eb49178.png)

## TLDR
- If you want precinct-level results for all of California for statewide races in the Nov. 8, 2016, election, look in the “final-results” directory.
- If you want California precinct shapefiles by county, look in the “shapefiles” directory.

## What is this?

We at the Los Angeles Times Data Viz team wanted to make the most detailed California election maps ever. To do that we had to work with each of the 58 counties. The secretary of state DOES NOT keep precinct-level results. The good folks at [Statewide Database at U.C. Berkeley Law](http://statewidedatabase.org) do organize these results, but not until at least six months after the election. We wanted to publish as soon as possible.

The layout of this repo is a little messy (sorry). Each county has a folder with its three-digit FIPS code. Inside you should find the original shapefile, consolidation documents (if needed) and results. These folders are where we did our work, so there may be other files in them like parsers, preliminary results, unprojected shapefiles or other scripts. Those scripts are buggy, probably crappy, and not intended to output a standard format or final data. If you use them, it’s at your own risk — be sure to check your results.

Inside “shapefiles,” you'll find the finalized, consolidated precinct shapefiles for each county. Join these together if you want to do the whole state.

In QGIS, go to Vector > Data Management Tools > Merge Shapefiles to One…

![screen shot 2016-12-29 at 5 28 28 pm](https://cloud.githubusercontent.com/assets/695934/21558288/3fa2a198-cdec-11e6-90be-0e836d87b13f.png)

Run this ogr2ogr from your command line:

```
for f in shapefiles/*.shp; do ogr2ogr -update -append merged.shp $f -f "ESRI Shapefile"; done;
```

After that, you should be able to join with [all_precinct_results.csv](https://github.com/datadesk/california-2016-election-precinct-maps/blob/master/final-results/all_precinct_results.csv).

## Shapefiles
All map files in the “shapefiles” folder are projected in WGS 84 and contain two columns:
- pct16 (a STRING column named "pct16" with the 3-digit county FIPS code and precinct number. For example, a Los Angeles County precinct might read `037-0080052A`)
- area (area will be in square meters calculated under projection NAD83 / UTM zone 10N)


## Results
Results in the final-results directory will have the following fields:
- pct16
- pres_clinton
- pres_johnson
- pres_stein
- pres_trump
- pres_lariva
- pres_other
- ussenate_harris
- ussenate_sanchez
- prop51_yes
- prop51_no
- prop52_yes
- prop52_no
- prop53_yes
- prop53_no
- prop54_yes
- prop54_no
- prop55_yes
- prop55_no
- prop56_yes
- prop56_no
- prop57_yes
- prop57_no
- prop58_yes
- prop58_no
- prop59_yes
- prop59_no
- prop60_yes
- prop60_no
- prop61_yes
- prop61_no
- prop62_yes
- prop62_no
- prop63_yes
- prop63_no
- prop64_yes
- prop64_no
- prop65_yes
- prop65_no
- prop66_yes
- prop66_no
- prop67_yes
- prop67_no

For example, here are three lines from `091-sierra.csv`:
```
pct16,pres_clinton,pres_trump,pres_johnson,pres_stein,pres_lariva,pres_other,ussenate_harris,ussenate_sanchez,prop51_yes,prop51_no,prop52_yes,prop52_no,prop53_yes,prop53_no,prop54_yes,prop54_no,prop55_yes,prop55_no,prop56_yes,prop56_no,prop57_yes,prop57_no,prop58_yes,prop58_no,prop59_yes,prop59_no,prop60_yes,prop60_no,prop61_yes,prop61_no,prop62_yes,prop62_no,prop63_yes,prop63_no,prop64_yes,prop64_no,prop65_yes,prop65_no,prop66_yes,prop66_no,prop67_yes,prop67_no
091-4,15,31,7,2,1,1,20,16,25,25,38,12,26,24,35,14,25,25,13,42,28,19,30,18,27,21,17,27,17,30,18,32,8,46,31,22,15,34,23,19,19,29
091-12,49,98,14,6,0,3,75,40,53,117,88,75,91,66,91,68,68,96,82,87,87,77,105,57,69,84,47,114,58,94,49,117,51,117,86,85,60,104,80,74,75,94
```

Results with “-munged” appended to the filename additionally contain these fields:
- pres_clinton_per
- pres_trump_per
- pres_third_per
- pres_winner
- pres_margin
- votedensity
- prop51_yes_per
- prop51_no_per
- prop52_yes_per
- prop52_no_per
- prop53_yes_per
- prop53_no_per
- prop54_yes_per
- prop54_no_per
- prop55_yes_per
- prop55_no_per
- prop56_yes_per
- prop56_no_per
- prop57_yes_per
- prop57_no_per
- prop58_yes_per
- prop58_no_per
- prop59_yes_per
- prop59_no_per
- prop60_yes_per
- prop60_no_per
- prop61_yes_per
- prop61_no_per
- prop62_yes_per
- prop62_no_per
- prop63_yes_per
- prop63_no_per
- prop64_yes_per
- prop64_no_per
- prop65_yes_per
- prop65_no_per
- prop66_yes_per
- prop66_no_per
- prop67_yes_per
- prop67_no_per

For example, here are the first three lines from `079-san-luis-obispo-munged.csv`:
```
pct16,pres_clinton,pres_trump,pres_johnson,pres_stein,pres_lariva,pres_other,ussenate_harris,ussenate_sanchez,prop51_yes,prop51_no,prop52_yes,prop52_no,prop53_yes,prop53_no,prop54_yes,prop54_no,prop55_yes,prop55_no,prop56_yes,prop56_no,prop57_yes,prop57_no,prop58_yes,prop58_no,prop59_yes,prop59_no,prop60_yes,prop60_no,prop61_yes,prop61_no,prop62_yes,prop62_no,prop63_yes,prop63_no,prop64_yes,prop64_no,prop65_yes,prop65_no,prop66_yes,prop66_no,prop67_yes,prop67_no,pres_clinton_per,pres_trump_per,pres_third_per,pres_winner,pres_margin,votedensity,prop51_yes_per,prop51_no_per,prop52_yes_per,prop52_no_per,prop53_yes_per,prop53_no_per,prop54_yes_per,prop54_no_per,prop55_yes_per,prop55_no_per,prop56_yes_per,prop56_no_per,prop57_yes_per,prop57_no_per,prop58_yes_per,prop58_no_per,prop59_yes_per,prop59_no_per,prop60_yes_per,prop60_no_per,prop61_yes_per,prop61_no_per,prop62_yes_per,prop62_no_per,prop63_yes_per,prop63_no_per,prop64_yes_per,prop64_no_per,prop65_yes_per,prop65_no_per,prop66_yes_per,prop66_no_per,prop67_yes_per,prop67_no_per
079-CON101-01,425.0,791.0,55.0,25.0,9.0,20.0,534.0,445.0,575.0,721.0,731.0,545.0,659.0,593.0,755.0,507.0,626.0,665.0,569.0,744.0,669.0,622.0,821.0,466.0,469.0,740.0,472.0,772.0,415.0,847.0,373.0,913.0,452.0,859.0,669.0,639.0,574.0,698.0,751.0,483.0,582.0,703.0,32.08,59.7,8.23,trump,27.62,12.933280416945047,44.37,55.63,57.29,42.71,52.64,47.36,59.83,40.17,48.49,51.51,43.34,56.66,51.82,48.18,63.79,36.21,38.79,61.21,37.94,62.06,32.88,67.12,29.0,71.0,34.48,65.52,51.15,48.85,45.13,54.87,60.86,39.14,45.29,54.71
079-CON102-02,431.0,1133.0,59.0,13.0,2.0,33.0,721.0,462.0,615.0,988.0,890.0,698.0,866.0,689.0,973.0,595.0,728.0,865.0,681.0,966.0,809.0,804.0,991.0,619.0,601.0,927.0,548.0,1007.0,468.0,1104.0,360.0,1252.0,478.0,1150.0,894.0,754.0,635.0,960.0,946.0,586.0,712.0,893.0,25.79,67.8,6.4,trump,42.01,17.549261359524948,38.37,61.63,56.05,43.95,55.69,44.31,62.05,37.95,45.7,54.3,41.35,58.65,50.15,49.85,61.55,38.45,39.33,60.67,35.24,64.76,29.77,70.23,22.33,77.67,29.36,70.64,54.25,45.75,39.81,60.19,61.75,38.25,44.36,55.64
```




## Questions?
Contact [Jon Schleuss](https://twitter.com/gaufre) or [Joe Fox](https://twitter.com/joemfox) 
