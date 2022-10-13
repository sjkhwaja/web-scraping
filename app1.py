### import packages
import requests
from bs4 import BeautifulSoup
import pandas as pd

### pull website 
page = requests.get('https://www.billboard.com/charts/hot-100/')


### create beautifulsoup object
soup = BeautifulSoup(page.text, 'html.parser')

### get chart results
chart = soup.find_all('ul' , class_='lrv-a-unstyle-list lrv-u-flex lrv-u-height-100p lrv-u-flex-direction-column@mobile-max')


chart_results = []

for i in chart:
    print(i.text)
    data = i.text
    chart_results.append(data)

len(chart_results)
chart_results[2]
chart_results[10]

### get song rankings
rankings = soup.find_all('li' , class_='o-chart-results-list__item // lrv-u-background-color-black lrv-u-color-white u-width-100 u-width-55@mobile-max u-width-55@tablet-only lrv-u-height-100p lrv-u-flex lrv-u-flex-direction-column@mobile-max lrv-u-flex-shrink-0 lrv-u-align-items-center lrv-u-justify-content-center lrv-u-border-b-1 u-border-b-0@mobile-max lrv-u-border-color-grey')
	

song_ranking = []

for i in rankings:
    print(i.text)
    data = i.text
    song_ranking.append(data)

len(song_ranking)
song_ranking[2]
song_ranking[10]

### create dataframe with info
df = pd.DataFrame({'song_and_artist' : chart_results, 'ranking' : song_ranking})
df.to_csv('data/billboard.csv')