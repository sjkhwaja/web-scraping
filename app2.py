### import packages
import requests
from bs4 import BeautifulSoup
import pandas as pd

### pull website
page = requests.get('https://www.porsche.com/usa/modelstart/all/?modelrange=taycan')

### create soup object
soup = BeautifulSoup(page.text, 'html.parser')

### get car models
cars = soup.find_all('div' , class_='m-14-model-name')

models = []

for i in cars:
    print(i.text)
    data = i.text
    models.append(data)

len(models)
models[3]
models[23]

### get price of cars
price = soup.find_all('div' , class_='m-14-model-price')

prices_ = []

for i in price:
    print(i.text)
    data = i.text
    prices_.append(data)

len(prices_)
prices_[3]
prices_[23]

### create df to csv
df = pd.DataFrame({'porsche_model': models , 'starting_price': prices_})
df.to_csv('data/car_models.csv')

