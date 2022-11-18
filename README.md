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


## Reasearch Question and methodology:

### PART 1 : Global analysis of sport videos and NBA videos available on the `Youniverse` dataset.
- What is the evolution of the number of videos on Youtube within the study period ?
    - Among all these videos, what is the proportion of videos discussing about sport ?
    - Can we see an infatuation of the sport videos, and more precisely about basketball ?
- Is there a tendency in the length of sport videos (and of NBA related videos) ?
- How does the NBA calendar impact NBA videos on youtube ? Is there seasonality in the views of basketball videos ?
- Are baskeball and NBA videos more commented, liked or disliked than other sports ?


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
| Attendance | Time | Visitor | V PTS | Home | H PTS | Playoffs ? | V Pop | H Pop | Last Five | Capacity | Curr win % | Day of the week | Month | Match-ups | Rivalry | LS Win % |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
12884|1990-01-02|Miami Heat|95|Portland Trail Blazers|119|0|2|2|3|12884|0.6923076923076923|Tuesday|January|"frozenset({'Portland Trail Blazers'| 'Miami Heat'})"|0|0.4533333333333333
15025|1990-01-02|Utah Jazz|120|Golden State Warriors|133|0|4|3|3|15025|0.6153846153846154|Tuesday|January|"frozenset({'Utah Jazz'| 'Golden State Warriors'})"|0|0.6790123456790124
11676|1990-01-02|Milwaukee Bucks|107|Atlanta Hawks|113|0|2|5|4|16371|0.5185185185185185|Tuesday|January|"frozenset({'Atlanta Hawks'| 'Milwaukee Bucks'})"|0|0.581081081081081
19938|1990-01-03|Chicago Bulls|93|Cleveland Cavaliers|87|0|17|2|1|20273|0.3333333333333333|Wednesday|January|"frozenset({'Cleveland Cavaliers'| 'Chicago Bulls'})"|1|0.6710526315789473

We also have a table called `teams`that provides details about all NBA teams.
|full name | abbreviation | nickname | city | state | year_founded |
|---|---|---|---|---|---|
Atlanta Hawks|ATL|Hawks|Atlanta|Atlanta|1949
Boston Celtics|BOS|Celtics|Boston|Massachusetts|1946
Chicago Bulls|CHI|Bulls|Chicago|Illinois|1966
Cleveland Cavaliers|CLE|Cavaliers|Cleveland|Ohio|1970

## Proposed timeline


## Organization within the team: A list of internal milestones up until project Milestone P3.

ple around the globe. However, studying the platform is difﬁ-cult due to the lack of randomly sampled data and of system-atic ways to query the platform’s colossal catalog. In this pa-per, we present YouNiverse, a large collection of channel andvideo metadata from English-language YouTube. YouNiversecomprises metadata for over 136k channels and 72.9M videospublished between May 2005 and October 2019, as wellas channel-level time-series data of weekly subscriber andview counts. Leveraging channel ranks from socialblade.com,an online service that provides information about YouTube,we are able to assess and enhance the representativeness ofthe sample of channels. Additionally, the dataset also con-tains a table specifying which videos a set of 449M anony-mous users commented on. YouNiverse, publicly availableat https://doi.org/10.5281/zenodo.4650046, will empower thecommunity to do research with and about YouTube.

With the rise of YouTube since 2005, content creators rose to fame with an expanding follower base. Businesses saw this as an opportunity to sponsor their content, exploring marketing potential with creators. Nowadays, sponsorships are a common practice on the platform with many YouTubers making a living off of them.

But this practice does not come without its downsides. Spectators paying for a premium YouTube subscription are often annoyed by the ads that are forced upon them by their favorite YouTubers. Many creators have been accused of promoting services that they do not believe in, or even worse, that may be harmful to their audience.

This project aims to explore the relationship between YouTubers and their sponsors, and to determine whether or not sponsorships are beneficial to content creators. We hope to provide YouTubers with more information about their potential sponsors, and help them make more informed decisions.


## Overview
Here's a list of the relevant source files 

|Source file | Description|
|---|---|
|`notebook1.ipynb`           | The notebook you can run |
|`notebook2.ipynb`           | The notebook you can run |
|`notebook3.ipynb`           | The notebook you can run |
|`notebook4.ipynb`           | The notebook you can run |
|`notebook5.ipynb`           | The notebook you can run |

