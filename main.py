import csv
import requests
from bs4 import BeautifulSoup
import pandas as pd

HEADER = ['name', 'product_url', 'price', 'state', 'itemShopInfo']
category = input("guitar:1 bass:2 effector:3")
digimart = "https://www.digimart.net"

if category == "1":
  base_url = "https://www.digimart.net/cat01/"
elif category == "2":
  base_url = "https://www.digimart.net/cat03/"
else:
  base_url = "https://www.digimart.net/cat13/"

html = requests.get(base_url)
soup = BeautifulSoup(html.content, 'html.parser')
products = soup.find_all("li", class_="ProductBox")

with open('products.csv', 'w', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(HEADER)
    for product in products:
      product_classname = product.get("class")
      name = product.find("p",  attrs={'class': 'ttl'}).text
      url =  product.find("a").get('href')
      product_url = str(digimart) + str(url)
      price = product.find("p", attrs={'class': 'price'}).text
      state = product.find("p", attrs={'class': 'state'}).text
      itemShopInfo = product.find("p", attrs={'class': 'itemShopInfo'}).text
      row = [name, product_url, price, state, itemShopInfo]
      writer.writerow(row)

df = pd.read_csv('products.csv')
print(df)