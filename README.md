# Applied Data Analysis - Project ADACONDA - 2022-2023

The purpose of this project is to analyze the [Youniverse](https://zenodo.org/record/4650046) database and to measure the impact of important NBA events on Youtube videos.


## Team Members
ABI FADEL Zad: zad.abifadel@epfl.ch <br/>
ADEYE Abiola: abiola.adeye@epfl.ch <br/>
BRUNO Etienne: etiene.bruno@epfl.ch <br/>
FERCHIOU Sami: sami.ferchiou@epfl.ch <br/>


## Abstract

With the rise of Youtube since 2005, the number of videos available on the internet tremendously grew. Youtube became thus, a source for all kind of topics. This project intends to investigate and obtain insights on NBA (National Basketball Association) teams' popularity on Youtube. Based on the Youniverse dataset *(Ribeiro, Manoel Horta and West Robert)* and on multiple NBA sources (ranging from websites that we scraped and endpoints/APIs that we used), our analysis aims to help NBA teams be more popular on Youtube and use this platform to get useful insights before taking important decisions.  
In the first part, we try to get a global view of the Youniverse dataset and mainly the evolution of sport videos and more precisely NBA related videos. Therefore, we will examine the overall tendencies for views, comments and likes that appear within the subset of NBA related videos on Youtube compared to other sports videos.  
In a further analysis, we will focus on how popularity of NBA videos correlate with a teams' results, victory percentage and other important events of the NBA calendar (e.g. star players changing teams, start of the playoffs). This part focuses on the driving forces behind popularity of teams. This popularity will be assessed based on the Youniverse Dataset as well as data from the Google Trends API and attendance numbers for games scraped from the web.
Finally, we study how players and internal strategies within NBA teams interact with their popularity on Youtube. 

## NBA overview
The **National Basketball Association (NBA)** is the world's most famous basketball league. Thirty American and Canadian teams compete amongst each other during an 82 game-long **regular season**.  
At the end of the regular season, the top 8 teams in each conference (East & West) participate in a knockout tournament famously called the **playoffs**.  
At the end of the season, the winning team is crowned as the championship winner, a single player is awarded the **Most Valuable Player (MVP)** trophy, and an all-star team with the bes players from each conference is formed for an exhibition game during the **All-Star** weekend.  
The NBA season usually starts around October/November and ends around April/June/July. In addition to that, the playoffs start date is usually in May.
  


## Research questions and Methodology:

### PART 1 : Global analysis of sport videos and NBA videos available on the `Youniverse` dataset.
- What is the evolution of the number of videos on Youtube within the study period ?
    - Among these videos, what is the proportion of videos discussing about sport ?
- Is there a tendency in the length of sport videos (and of NBA related videos) ?
- Can we see an infatuation in the popularity of sports videos, and more precisely about NBA ?
- How does the NBA calendar impact NBA videos on youtube ? Is there seasonality in the views of basketball videos ?
- Are basketball and NBA videos more commented, liked or disliked than other sports ?

> In this first part, we have used Dask to load the datasets. 
> DASK is a distributed data processing framework that's optimized to handle very big files. It implements a big part of the Pandas API which allows us to get very similar queries to what we would in Pandas. Under the hood it uses several Pandas data-frames, a scheduler and worker nodes in order to handle the computations. One major benefit of DASK is that computations are carried out lazily which means that DASK creates a computation tree and only does the actual computation when we explicitly tell it to.
> We initially decompressed all gzip files locally to use Dask. This is because gzip does not use block-compression and therefore we can't load the data directly from the archive.
>  With Dask, we loaded all `.tsv` files and stored them in `.parquet` format. Parquet gives us several benefits compared to csv/tsv files:
> - Parquet uses block-compression by default which allows us to get files that are almost as small as the initial archives but that can be loaded directly into dask
> - Parquet is a columnar data storage format. This allows us to open only a subset of columns from the datasets which makes the initial loading operation considerably faster.
> All details about this initial process can be found in the jupyter notebook called `1_data_loading_and_pre_processing.ipynb`


> We explored the option of converting the Youniverse dataset to a local or hosted SQL database. In order to do that we loaded the data by chunks and saved them to the database. This approach requires a lot of storage (approximately 500 GB of data). Even though this approach is appealing because it allows us to build indices and create views in order to make our queries efficient, we decided to go against it and to work with DASK.

### PART 2 : Impact of the performances of NBA teams.
- What is the impact of the main NBA matches and results on Youtube video interactions ?
- How do the fans react to a good/bad performance of a team ? Do the fan interactions on NBA Youtube videos change following a victory or defeat of their respective team ? (fans : people frequently interacting with a certain NBA team on Youtube)
- How much does the results of a team impact the engagement of its fans for big market teams and small market team ? (popularity is measured with the number of like, dislikes, number of views and comments, attendance numbers and trends on google) 
- Are NBA fans usually following a single team or the whole championship ?
- Are small market teams fans more loyal than big market teams ? Do fans still follow their team even if the it's results are not good ? (Small/Big market teams : NBA teams are characterized by their market size, i.e. big market teams usually represent big cities such as New York/Chicago, where as small market teams usually represents small cities or cities where basketball is not an important sport such as New Orleans/Memphis)


### PART 3 : In depth analysis within NBA teams
- Are some players more popular than their own team ? Is it the popularity of the players that improves the popularity of a team ? 
- How do NBA teams manage to be more popular ? Is this popularity affecting their results ? 
- Is the championship MVP always the most popular player? (MVP : Most Valuable Player) 

- Additional questions :
    - Is there a fan base in each NBA Team ?
    - Is the popularity of a player more related to his level or to the popularity of his team ? 
    - Are offensive teams, that score many points during their matches, more popular than defensive teams ? (i.e. Basketball teams can play with         different tactics and thus score more or less points during a certain match, independently of the final result of the match) 
    - Can we predict the players’ transfers based on their popularity ?
    - Do fans follow players or teams?


## Additional datasets
Here are the relevant additional APIs we used to get information we can link to the Youniverse dataset.
  - [NBA API](https://pypi.org/project/nba-api/) allows to obtain about game data (points, matches dates, teams info (nicknames, abbreviations, foundation year)...),
  - [Google Trend API](https://pypi.org/project/pytrends/) giving popularity data
  - Scraping from Wikipedia and other websites to obtain stadium data (location, attendance, ...)
This information is stored in SQL (SQLite) database hosted on our computer. This database is then used to query any information related to the performances of the NBA teams. This is mostly used in the second part of the project where we investigate the relation between teams' performances and the popularity of NBA videos on youtube.

For the example, our largest table is called `game_data` and has the following columns:
| visitor | visitor\_points | home | home\_points | overtime | attendance | arena | time | playoffs | season | last\_five | season\_high\_attendance | curr\_season\_win\_pct | last\_5 | last\_10 | last\_15 | previous\_season\_win\_pct | previous\_regular\_season\_win\_pct |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Golden State Warriors | 108 | Cleveland Cavaliers | 85 |  | 20562 | Quicken Loans Arena | 2018-06-08 21:00:00 | 1 | 2018 | 0 | 20562 | 0.5961538461538461 | 1 | 4 | 8 | 0.64 | 0.64 |
| Golden State Warriors | 110 | Cleveland Cavaliers | 102 |  | 20562 | Quicken Loans Arena | 2018-06-06 21:00:00 | 1 | 2018 | 0 | 20562 | 0.6019417475728155 | 2 | 4 | 9 | 0.64 | 0.64 |
| Cleveland Cavaliers | 103 | Golden State Warriors | 122 |  | 19596 | Oracle Arena | 2018-06-03 20:00:00 | 1 | 2018 | 0 | 19596 | 0.7128712871287128 | 4 | 7 | 11 | 0.8383838383838383 | 0.8383838383838383 |
| Cleveland Cavaliers | 114 | Golden State Warriors | 124 | OT | 19596 | Oracle Arena | 2018-05-31 21:00:00 | 1 | 2018 | 0 | 19596 | 0.71 | 3 | 7 | 10 | 0.8383838383838383 | 0.8383838383838383 |
| Golden State Warriors | 101 | Houston Rockets | 92 |  | 18055 | Toyota Center | 2018-05-28 21:00:00 | 1 | 2018 | 0 | 18476 | 0.7676767676767676 | 2 | 6 | 9 | 0.6559139784946236 | 0.6559139784946236 |




We also have a table called `teams` that provides details about all NBA teams.
|full name | abbreviation | nickname | city | state | year_founded |
|---|---|---|---|---|---|
Atlanta Hawks|ATL|Hawks|Atlanta|Atlanta|1949
Boston Celtics|BOS|Celtics|Boston|Massachusetts|1946
Chicago Bulls|CHI|Bulls|Chicago|Illinois|1966
Cleveland Cavaliers|CLE|Cavaliers|Cleveland|Ohio|1970


## Proposed timeline
|Date | Objective|
|---|---|
| 25-11-2022 | Implementation of parts I and II ready |
| 02-12-2022 | Implementation and analysis of parts I and II |
| 09-12-2022 | Implementation of part III |
| 16-12-2022 | Website construction and story telling |
| 23-12-2022 | M3 ready and submission |

## Organization within the team: a list of internal milestones up until project Milestone P3.
- Abiola
    - Data loading and pre-processing using Dask
    - Impact of real NBA calendar and matches on Youtube views (engagement of fans, on both big and small market teams)
    - Loyalty of small teams and big teams 
    - Popularity of the MVP player
- Etienne
    - General analysis on sport videos
    - Tendencies on basketball and NBA videos on Youtube
    - Analysis results for offensive and defensive teams 
    - Popularity of players versus popularity of teams
- Sami
    - Analysis of the impact of the main NBA matches and results on Youtube video interactions
    - Reaction of fans following a good / bad match
    - Criteria for a team to be popular
- Zad
    - Data scraping from website and NBA API
    - Study of the comments, likes and dislikes of NBA related videos.



## Overview
Here's a list of the relevant source files 

|Source file | Description|
|---|---|
|`1_data_loading_and_pre_processing.ipynb`           | Notebook used to load the data from uncompressed files and save them into parquet files|
|`2_google_trends_api_database_creation.ipynb`           | Notebook to load popularity of teams from Google trends API |
|`2_nba_database_creation.ipynb`           | Notebook to scrape data from NBA websites and APIs and save them into a local SQL (SQLite) Database |
|`3_data_exploration.ipynb`           | Notebook where the first data exploration is made and the first research questions are answered|
|`4_data_case_study.ipynb`           | Notebook where we do a case study comparing impact of winning percentage of Small and Big market teams |

