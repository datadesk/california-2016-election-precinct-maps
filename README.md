# California's most detailed election result map EVER

We at the Los Angeles Times Graphics Desk wanted to make the most detailed maps of the 2016 election possible. To do that we had to work with each county. The secretary of state DOES NOT keep precinct-level results. But the good folks at [Statewide Database at U.C. Berkeley Law](http://statewidedatabase.org) do organize these results. But not until at least six months after the election. 

The layout of this repo is a little messy. Each county has a folder with its three-digit FIPS code. Inside you'll find the original shapefile, any consolidation documents and the results. 

Inside ready-precincts and for-merge you'll find the finalized precinct shapefiles for each county. Join these together if you want to do the whole state.

Similarly the results are stored in separate files for each county in the final-results folder. They have a base file, a "munged" file and a "munged" CSVT file. Use the "munged" file for results, because it contains the percentage of voters and vote density for each precinct, including the winner of the presidential race.

## Questions?
Contact [Jon Schleuss](https://twitter.com/gaufre) or [Joe Fox](https://twitter.com/joemfox) 



## Shapefiles
All shapefiles should be projected in WGS 84 and contain two columns:
- pct16
- area (area will be in square meters if calculated under projection NAD83 / UTM zone 10N. Use field calculator to create a new field, type Decimal number (real), 20-length with 5-precision. Use "$area" under Geometry.)

## Workflow
Each county is going to be different based on how the data is formatted and where and when we get it. But these should be the basic steps:
  1. Get data from county
  2. Reformat data as comma-delimited file with column names that match our field template (see below)
  3. Use the "data munger" to add relevant columns to a new file
  4. Pull main csv from this github repo
  5. Append/merge your "munged" csv with the main csv
  6. Push file back to repo
  7. Replace current Carto table with new version of the main csv

## Data format
We'll stitch together all the (coastline-clipped) precincts as one WGS84 file that includes the shapes for the counties. Each feature must have a STRING column named "pct16" with the 3-digit county FIPS code and precinct number. For example, a Los Angeles County precinct might read `037-0080052A`

Results will need that same format for the unique precinct number and include the following fields:
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

A "data munger" script will add these fields:
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
