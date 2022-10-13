### import packages
import requests
from bs4 import BeautifulSoup
import pandas as pd

### pull website 
page = requests.get('https://www.billboard.com/charts/hot-100/')


### create beautifulsoup object
soup = BeautifulSoup(page.text, 'html.parser')

### get chart results
chart = soup.find_all('li' , class_='o-chart-results-list__item // lrv-u-flex-grow-1 lrv-u-flex lrv-u-flex-direction-column lrv-u-justify-content-center lrv-u-border-b-1 u-border-b-0@mobile-max lrv-u-border-color-grey-light lrv-u-padding-l-050 lrv-u-padding-l-1@mobile-max')


chart_results = []

for i in chart:
    print(i.text)
    data = i.text
    chart_results.append(data)

len(chart_results)
chart_results[2]
chart_results[10]

