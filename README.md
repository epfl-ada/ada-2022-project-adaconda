<h1 align="center">Applied Data Analysis - Project ADACONDA - 2022-2023 <img src="https://media.giphy.com/media/hvRJCLFzcasrR4ia7z/giphy.gif" width="35"></h1>
<p align="center">

The purpose of this project is to analyze the [Youniverse](https://zenodo.org/record/4650046) database and to measure the impact of important NBA events on Youtube videos.



## Team Members 🤝
ABI FADEL Zad: zad.abifadel@epfl.ch <br/>
ADEYE Abiola: abiola.adeye@epfl.ch <br/>
BRUNO Etienne: etiene.bruno@epfl.ch <br/>
FERCHIOU Sami: sami.ferchiou@epfl.ch <br/>



## Abstract ✍️
  
This article examines the the disparities in viewership between small and large market teams in the National Basketball Association (NBA). Using YouNiverse data from 2005 to 2019, we tracked videos containing the tags “NBA” and “Basketball” to measure the growth in viewership over the past decade. We then used data from the TV market size for each team to classify them into small, medium, and large markets. By studying a subset of 8 small and 8 large market teams, we found that there are still significant differences between the viewership of the two categories. We argued that this could be explained by differences in financial means, media exposure, and local fan base. Our findings provide insight into the impact of streaming platforms on the NBA’s viewership and how the league can improve its reach and appeal to viewers of all market sizes.



## NBA overview 🏀
The **National Basketball Association (NBA)** is the world's most famous basketball league. Thirty American and Canadian teams compete amongst each other during an 82 game-long **regular season**. At the end of the regular season, the top 8 teams in each conference (East & West) participate in a knockout tournament famously called the **playoffs**. At the end of the season, the winning team is crowned as the championship winner, a single player is awarded the **Most Valuable Player (MVP)** trophy, and an all-star team with the bes players from each conference is formed for an exhibition game during the **All-Star** weekend. The NBA season usually starts around October/November and ends around June/July. In addition to that, the playoffs start date is usually in May.
  


## Research questions and Methodology 📚

### PART 1 : GLOBAL ANALYSIS OF SPORT VIDEOS AND NBA VIDEOS AVAILABLE ON THE `YOUNIVERSE` DATASET.
- Filter Youtube videos that only contains specifics tags
- What is the evolution of the number of videos on Youtube within the study period ?
- Among these videos, what is the proportion of videos discussing about sport ?
- Is there a tendency in the length of sport videos (and of NBA related videos) ?
- Can we see an enthusiasm in the popularity of sports videos, and more precisely about NBA ?


### PART 2 : BIG VS SMALL MARKET TEAMS
- How do the differences between small and big market teams affect player recruitment and retention? (competitive advantages of small and big market teams in the NBA)
- What factors have contributed to the success of small market or big market teams in the views of Youtube videos?
- What is the impact of a star player on the Youtube views of a team ?
- Does the number of YouTube views of NBA teams correlate with their performance in the regular season?


### PART 3 : MEDIA EXPOSURE OF NBA TEAMS (SMALL AND BIG)
- How are NBA teams represented on the social medias ? 
- Is the media exposure of big market teams greater than that of small market teams ? 
- How can we measure the media exposure of an NBA team on Youtube ? 
- Is there bias that push people to follow a certain team instead of another ? 
- Is the engagement of the fans similar for big and small market teams ? 



## Additional datasets 💻
Here are the relevant additional APIs we used to get information we can link to the Youniverse dataset.
  - [NBA API](https://pypi.org/project/nba-api/) allows to obtain about game data (points, matches dates, teams info (nicknames, abbreviations, foundation year)...),
  - [NBA TV Market size](https://www.sportsmediawatch.com/nba-market-size-nfl-mlb-nhl-nielsen-ratings/) NBA Team Market Size Rankings 2022
  - [NBA Free Agent Tracker](https://www.nba.com/players/free-agent-tracker/2021?dir=D&sort=PPG) NBA Player Movement 2022
2022 Free Agency
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



## Organization within the team: a list of internal milestones :clock10:
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
    - Number of videos per team and market size
    - Story telling
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

