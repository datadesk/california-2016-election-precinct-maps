# California's most detailed election result map EVER

We're gonna make a precinct-level map of results from the 2016 General Election. And we're gonna do it within 24 hours of polls closing.

[Google Spreadsheet with current status](https://docs.google.com/spreadsheets/d/1_4YN6v-GzB5s8DQ7JbImkeJAqj-o3DrISaB7aS-PHHA/edit?usp=drive_web)

These results will power these projects
- How many people near you voted to...[elect Trump|elect Clintion|legalize weed|etc.]
- 2016: The year Orange County turned blue
- Support of the repeal of the death penalty
- Perscription drugs costs
- Gun control
- Legalizing recreational marijuana
- Mapping support/opposition of L.A. County measures A and M, School issue CC and L.A. city issues HHH, JJJ, RRR and SSS.

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
- pres_clinton
- pres_johnson
- pres_lariva
- pres_stein
- pres_trump
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

## County status
| county          | shapefile?        | results?                                            |
|-----------------|-------------------|-----------------------------------------------------|
| Alameda         | ![yes] yes      | ![yes] yes, [should be online](http://www.acgov.org/rov/elections/20161108/)      |
| Alpine          | ![yes] yes      |    ![yes] yes, [online](http://www.alpinecountyca.gov/index.aspx?NID=388)                    |
| Amador          | ![yes] yes        | ![yes] yes, [online](http://amadorgov.org/government/elections/election-results)      |
| Butte           | ![maybe] soon       | ![yes] yes, [online](http://clerk-recorder.buttecounty.net/elections/electhome.html)  |
| Calaveras       | ![no] no              | ![no] none until certified                                |
| Colusa          | ![yes] yes          | ![yes] yes, will need to call 530-458-0500                       |
| Contra Costa    |                   |                                                     |
| Del Norte       | ![maybe] Tommy making | ![yes] yes, call                                  |
| El Dorado       | ![maybe] Jon to consolidate    | ![yes] yes, will provide a CSV on election night |
| Fresno          | ![yes] yes      | ![no] not until 3 weeks after election                        |
| Glenn           | ![yes] yes          | ![yes] yes, [online](http://www.countyofglenn.net/dept/elections/voting-results)      |
| Humboldt        | ![yes] yes       | ![yes] yes, [online](http://www.humboldtgov.org/Archive.aspx?ADID=1081)    |
| Imperial        | ![maybe] waiting      |  ![no] none until certified                                           |
| Inyo            | ![yes] yes    | ![yes] yes, [online](http://elections.inyocounty.us/p/election-results.html)  |
| Kern            | ![yes] yes        | ![no] no, but could call and get Nov. 10   |
| Kings           | ![maybe] waiting               |                                                     |
| Lake            | ![yes] yes        |  ![no] none until certified                                  |
| Lassen          | ![no] print maps only     | ![no] none until certified, one week after election       |
| Los Angeles     | ![yes] yes               | ![yes] afternoon of Nov. 9                                 |
| Madera          |                   | ![no] no                                                  |
| Marin           | ![yes] yes       | ![no] no, but [eventually online](http://www.marincounty.org/depts/rv/election-info/past-elections) |
| Mariposa        | ![yes] yes       | ![yes] yes, they'll give it to us on Nov. 9 |
| Mendocino       | ![maybe] Tommy making  | ![no] not until certified |
| Merced          |                   |                                                     |
| Modoc           | ![yes] yes            |    ![yes] yes on their website                                 |
| Mono            | ![yes] yes        | ![yes] yes, day after or [after midnight online](http://www.monocounty.ca.gov/elections/page/election-results) |
| Monterey        | ![yes] yes               | ![no] no: county-wide results only                        |
| Napa            | ![maybe] Tommy making  |  ![no] not until certified  |
| Nevada          | ![yes] yes   |  ![yes] yes, they'll email to Jon        |
| Orange          | ![yes] yes |  ![yes] statement of votes cast pdf on site http://www.ocvote.com/ |
| Placer          | ![yes] yes | ![yes] yes, [online](http://www.placerelections.com/past-elections.aspx#060716)   |
| Plumas          | ![yes] yes        |  ![yes] yes, [pdf online](http://www.plumascounty.us/index.aspx?NID=147)   |
| Riverside       | ![yes] yes | ![yes] Yes, live on http://www.voteinfo.net/ |
| Sacramento      | ![yes] yes               |                                                     |
| San Benito      | ![yes] yes             | ![yes] Yes, live on http://sbcvote.us/ in tabular pdf form |
| San Bernardino  | ![yes] yes               | ![yes] yes, will email to Jon                              |
| San Diego       | ![yes] yes               | ![no] no-available later that week                        |
| San Francisco   |  ![yes] yes| ![yes] three waves night of election, updates 4pm every day till certification (http://sfgov.org/elections/data-results-maps-and-archives)|
| San Joaquin     |           | ![no] Do not do preliminary results - available 28 days after the election on website                                                    |
| San Luis Obispo |  ![yes] yes  | ![yes] yes-Available Nov. 9                                |
| San Mateo       |                  |                                                   |
| Santa Barbara   | ![yes] yes Jon created     | ![yes] yes, [online](http://www.sbcvote.com/elections/UpcomingElections.aspx)    |
| Santa Clara     |                   |                                                     |
| Santa Cruz      | ![yes] yes  | ![yes] yes, [should be online](http://www.votescount.com/Home/UpcomingElections/November8,2016PresidentialGeneralElection.aspx)      |
| Shasta          | ![yes] yes         | ![yes] yes, [online](http://www.elections.co.shasta.ca.us/election-results/election-results/current-election-results/)     |
| Sierra          | ![yes] yes                | ![yes] yes                                                 |
| Siskiyou        | ![yes] Yes               | ![no] None until certified                                |
| Solano          | ![maybe] waiting  | ![no] None until certified                  |
| Sonoma          |                   | ![no] None until cerified                                                    |
| Stanislaus      | ![yes] yes | ![yes] yes, [online](http://stanvote.com/past-results/results.htm)        |
| Sutter          | ![yes] yes |                                                     |
| Tehama          | ![yes] yes        |                                                     |
| Trinity         | ![no] "not anytime soon" | ![maybe] possible after election  |
| Tulare          | ![maybe] waiting | ![no] not until certified             |
| Tuolumne        | ![no] no       | ![no] not until certified              |
| Ventura         | ![yes] yes         |  ![yes] yes [online](http://recorder.countyofventura.org/elections/election-resultscanvass-of-the-vote/)  |
| Yolo            | ![no] no                | ![maybe] Live updated at http://www.yoloelections.org/       |
| Yuba            | ![yes] yes          | ![no] not until certified                          |


[yes]: https://cloud.githubusercontent.com/assets/695934/19056263/f95b9a40-897c-11e6-99b6-d8348a071b0e.png
[maybe]: https://cloud.githubusercontent.com/assets/695934/19056262/f958961a-897c-11e6-93fd-40f39602a9a5.png
[no]: https://cloud.githubusercontent.com/assets/695934/19056261/f9586dca-897c-11e6-8b7e-e9606a05f5ee.png
