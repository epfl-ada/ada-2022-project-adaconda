# Applied Data Analysis - Project ADACONDA - 2022-2023

The purpose of this project is to analyse the [Youniverse](https://zenodo.org/record/4650046) database and to measure the impact of important NBA events on Youtube videos.


## Team Members
ABI FADEL Zad: zad.abifadel@epfl.ch <br/>
ADEYE Abiola: abiola.adeye@epfl.ch <br/>
BRUNO Etienne: etiene.bruno@epfl.ch <br/>
FERCHIOU Sami: sami.ferchiou@epfl.ch <br/>


## Abstract
<p align="justify">
With the rise of Youtube since 2005, the number of videos available on the internet tremendously grew. Youtube became a source for all kind od topics. This project intends to investigate the connection between NBA (National Basketball Association) videos available in our datasets (from 2006 to 2019) and some metrics of these NBA teams. In a first part, we try to get a global view of the dataset and mainly the evolution of sport videos and we compare it this development with the progression of NBA related videos. More precisely, we examine the overall tendencies that appear with time such as duration of sport and basketball videos or the interaction with these videos. In a further analysis we focus on the study of NBA videos and how they correlate with results, victory percentage and important events of NBA teams. This objective is to measure how key points impact popularity of teams and their videos on the Youniverse dataset. Finally, in a third part, ...
</p>


## Reasearch questions and Methodology:

### PART 1 : Global analysis of sport videos and NBA videos available on the `Youniverse` dataset.
- What is the evolution of the number of videos on Youtube within the study period ?
    - Among all these videos, what is the proportion of videos discussing about sport ?
    - Can we see an infatuation of the sport videos, and more precisely about basketball ?
- Is there a tendency in the length of sport videos (and of NBA related videos) ?
- How does the NBA calendar impact NBA videos on youtube ? Is there seasonality in the views of basketball videos ?
- Are baskeball and NBA videos more commented, liked or disliked than other sports ?

> To investigate this first part, we have used Dash to load the datasets. We initially decompressed all gzip files locally to use Dask. With Dask, we hence loaded all `.tsv` file and stored them in `.parquet` file which allows us to get file as light as `.gzip` file but readable by Dask (by contrast with `.gzip` file which are not readable by Dask). Dask allows us to use lazy valuation and to use mutliple cores which means that the variable is not computed until the function is called followed by `.compute()` and when it is computed, it is ditributed on all the allocated cores. Furthermore, when a variable is regularly used, we can use the `.persist()` to keep it in memory. This allows us to compute it only once and be able to use it according to our needs. All details about this initial process can be found in the jupyter notebook called `1_data_loading_and_pre_processing.ipynb`

> In addition to dask, we also investigate the possibility to store all of our data in a local database when we will futher get data using SQL queries. The implementation where we loaded all the data by chunks and store them in the database can be found in the jupyter notebook titled `.2_database_creation.ipynb`. However the main drawback of this methods is that files are not compressed so it required more memory space on the hardrive (nearly 500 Go) and we cannot benefit from the parrallelization on mutliple cores. For these two reason, we have decided to pursue the project using Dask and to keep the database for verification purposes.


### PART 2 : Impact of the performances of NBA team.
- What the impact of the main NBA matches and results on Youtube video interactions ?
- How do fans react to a bad performance of a team ?
- How much does the results of a team impact the engagement of its fans for big market teams and small market team ? (popularity is measured with the number of like, dislikes, number of views and comments)
- Are small market teams fans more loyal than big market teams ? (fans : people frequently interacting with a certain NBA team on Youtube)


### PART 3 : In depth analysis within teams
- Are some players more popular than their own team ?
- Interaction of fans with NBA Youtube videos
    - How do the fans react to a bad performance of a team ?
    - Are NBA fans following a single team or all of them ?
- How does NBA teams manage to be more popular ? Is this popularity affecting their results ? 
- Is the MVP always the most popular player ?

- If we have time:
    - Is there a fan base in each NBA Team ?
    - Are NBA team following a single team or all of them ?
    - Can we predict the player’s transfers based on their popularity ?


## Additional datasets
We used addional API to get infornation we can link to the Youniverse dataset.
  - [NBA API](https://pypi.org/project/nba-api/) allows to obtain about game data (points, matches dates, teams info (nicknames, abbreviations, foundation year)...),
  - [Google Trend API](https://pypi.org/project/pytrends/) giving popularity data
  - Scrapping from wikipedia to obtain, using Beautiful Soup, stadium data (location, attendance)
With this information, we have create a new SQL database hosted on our computer. This database is then used to query any information related to the performances of the NBA teams. This is mostly used in the second part of the project where we investigate the relation between teams' performances and the popularity of NBA videos on youtube.

For the example, our largest table is called `game_data` and has the following columns:
| visitor | visitor_points | home | home_points | overtime | attendance | arena | time | season | last_five | seasson_high_attendance | curr_season_win_pct | last_5 | last_10 | last_15 | previous_season_win_pct | previous_regular_season_win_pct
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
Denver Nuggets|97|Phoenix Suns|102|""|17852|America West Arena|2005-12-02 21:00:00|0|2006|0|18422|0.6428571428571429|5|7||0.7319587628865979
Atlanta Hawks|94|Phoenix Suns|112|""|16992|America West Arena|2005-12-04 20:00:00|0|2006|0|18422|0.6666666666666666|5|8|10|0.7319587628865979
Portland Trail Blazers|85|Phoenix Suns|130|""|15102|America West Arena|2005-12-06 21:00:00|0|2006|0|18422|0.6875|5|8|11|0.7319587628865979
Denver Nuggets|100|Miami Heat|92|""|19896|AmericanAirlines Arena|2005-12-09 19:30:00|0|2006|0|20294|0.5|1|4|8|0.7216494845360825
New York Knicks|81|Phoenix Suns|85|""|18207|America West Arena|2005-12-09 22:00:00|0|2006|0|18422|0.7222222222222222|5|9|11|0.7319587628865979


We also have a table called `teams`that provides details about all NBA teams.
|full name | abbreviation | nickname | city | state | year_founded |
|---|---|---|---|---|---|
Atlanta Hawks|ATL|Hawks|Atlanta|Atlanta|1949
Boston Celtics|BOS|Celtics|Boston|Massachusetts|1946
Chicago Bulls|CHI|Bulls|Chicago|Illinois|1966
Cleveland Cavaliers|CLE|Cavaliers|Cleveland|Ohio|1970


## Proposed timeline


## Organization within the team: a list of internal milestones up until project Milestone P3.
- Abiola
    - Data laoding and pre-processing using dask
    - 
- Etienne
    - General analysis on sport videos
    - Tendencies on basketball and NBA videos on Youtube
- Sami
    - Analysis of the impact of the main NBA matches and results on Youtube video interactions
    - 
- Zad
    - Data scrapping from website and NBA API
    - 


## Overview
Here's a list of the relevant source files 

|Source file | Description|
|---|---|
|`1_data_loading_and_pre_processing.ipynb`           | The notebook used to load the data from uncompressed files and save them into parquet files|
|`2_database_creation.ipynb`           | Notebook to load data and save them into our local SQL Database |
|`3_data_exploration.ipynb`           | Notebook where the first data exploration is made and the first research questions are answered|
|`api_nba.ipynb`           | Notebook where we scrapped data from websites and used NBA api to get data about NBA teams and matches |

