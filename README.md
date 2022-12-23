<h1 align="center">Applied Data Analysis - Project ADACONDA - 2022-2023 <img src="https://media.giphy.com/media/hvRJCLFzcasrR4ia7z/giphy.gif" width="35"></h1>
<p align="center">

The purpose of this project is to analyze the [Youniverse](https://zenodo.org/record/4650046) database and to measure the impact of important NBA events on Youtube videos.


## Team Members
ABI FADEL Zad: zad.abifadel@epfl.ch <br/>
ADEYE Abiola: abiola.adeye@epfl.ch <br/>
BRUNO Etienne: etiene.bruno@epfl.ch <br/>
FERCHIOU Sami: sami.ferchiou@epfl.ch <br/>


## Abstract

This article examines the the disparities in viewership between small and large market teams in the National Basketball Association (NBA). Using YouNiverse data from 2005 to 2019, we tracked videos containing the tags “NBA” and “Basketball” to measure the growth in viewership over the past decade. We then used data from the TV market size for each team to classify them into small, medium, and large markets. By studying a subset of 8 small and 8 large market teams, we found that there are still significant differences between the viewership of the two categories. We argued that this could be explained by differences in financial means, media exposure, and local fan base. Our findings provide insight into the impact of streaming platforms on the NBA’s viewership and how the league can improve its reach and appeal to viewers of all market sizes.

## NBA overview
The **National Basketball Association (NBA)** is the world's most famous basketball league. Thirty American and Canadian teams compete amongst each other during an 82 game-long **regular season**. At the end of the regular season, the top 8 teams in each conference (East & West) participate in a knockout tournament famously called the **playoffs**. At the end of the season, the winning team is crowned as the championship winner, a single player is awarded the **Most Valuable Player (MVP)** trophy, and an all-star team with the bes players from each conference is formed for an exhibition game during the **All-Star** weekend. The NBA season usually starts around October/November and ends around June/July. In addition to that, the playoffs start date is usually in May.
  


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


### PART 2 : Impact of the performances of NBA teams.
- How do the fans react to a good/bad performance of a team ? Do the fan interactions (likes/comments/views) on NBA Youtube videos change following a victory or defeat of their respective team ? (fans : people frequently interacting with a certain NBA team on Youtube)
- How much does the results of a team impact the engagement of its fans for big market teams and small market team ? (engagement is measured with the number of like, dislikes, number of views and comments, attendance numbers and trends on google) 
- Are NBA fans usually following a single team or the whole championship ?
Are small market teams fans more loyal than big market teams ? Do fans still follow their team even if the it's results are not good ? (Small/Big market teams : NBA teams are characterized by their market size, i.e. big market teams usually represent big cities such as New York/Chicago, where as small market teams usually represents small cities or cities where basketball is not an important sport such as New Orleans/Memphis)


### PART 3 : In depth analysis within NBA teams
- Are some players more popular than their own team ? Is it the popularity of the players that improves the popularity of a team ? 
- Does the popularity of teams affect their results ? 
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


## Organization within the team: a list of internal milestones :raised_hands:.
- Abiola
    - Data loading and pre-processing using Dask
    - Data scraping from NBA (winning rates statistics)
    - Impact of the winning rates of teams on the Youtube views
    - Story telling
- Etienne
    - General analysis on sport videos : tendencies on basketball and NBA videos on Youtube
    - Impact of the winning rates of teams on the Youtube views 
    - Website creation and design
- Sami
    - Media exposure analysis of both small and big markets teams
    - Number of videos per team
    - Number of videos per market size
    - Number of fan-bases channels per team (quantification of engagement)
- Zad
    - Data scraping from websites and NBA API
    - Impact of real NBA transfers Youtube views (engagement of fans, on both big and small market teams)
    - Popularity of the MVP player



## Overview
Here's a list of the relevant source files 

|Source file | Description|
|---|---|
|`final_notebook.ipynb`           | Notebook used with all our data visualisations|

