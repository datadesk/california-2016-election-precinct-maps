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

## Data format
We'll stitch together all the (coastline-clipped) precincts as one WGS84 file that includes the shapes for the counties. Each feature must have a STRING column named "pct16" with the 3-digit county FIPS code and precinct number. For example, a Los Angeles County precinct might read `037-0080052A`

Results will need that same format for the unique precinct number and include the following fields:
- pres_clinton
- pres_johnson
- pres_lariva
- pres_stein
- pres_trump
- pres_other
- us_senate_harris
- us_senate_sanchez
- prop_51_yes
- prop_51_no
- prop_52_yes
- prop_52_no
- prop_53_yes
- prop_53_no
- prop_54_yes
- prop_54_no
- prop_55_yes
- prop_55_no
- prop_56_yes
- prop_56_no
- prop_57_yes
- prop_57_no
- prop_58_yes
- prop_58_no
- prop_59_yes
- prop_59_no
- prop_60_yes
- prop_60_no
- prop_61_yes
- prop_61_no
- prop_62_yes
- prop_62_no
- prop_63_yes
- prop_63_no
- prop_64_yes
- prop_64_no
- prop_65_yes
- prop_65_no
- prop_66_yes
- prop_66_no
- prop_67_yes
- prop_67_no

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
| San Francisco   |                   |                                                     |
| San Joaquin     |                   |                                                     |
| San Luis Obispo |  ![yes] yes  | ![yes] yes-Available Nov. 9                                |
| San Mateo       |                  |                                                   |
| Santa Barbara   | ![yes] yes Jon created     | ![yes] yes, [online](http://www.sbcvote.com/elections/UpcomingElections.aspx)    |
| Santa Clara     |                   |                                                     |
| Santa Cruz      | ![yes] yes         | ![yes] yes, [should be online](http://www.votescount.com/Home/UpcomingElections/November8,2016PresidentialGeneralElection.aspx)      |
| Shasta          | ![yes] yes         | ![yes] yes, [online](http://www.elections.co.shasta.ca.us/election-results/election-results/current-election-results/)     |
| Sierra          | ![yes] yes                | ![yes] yes                                                 |
| Siskiyou        | ![yes] Yes               | ![no] None until certified                                |
| Solano          | ![maybe] waiting  | ![no] None until certified                  |
| Sonoma          |                   |                                                     |
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
