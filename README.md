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

## Questions?
Contact [Jon Schleuss](https://twitter.com/gaufre) or [Joe Fox](https://twitter.com/joemfox) 
