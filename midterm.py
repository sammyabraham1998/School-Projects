#This code uses 3 methods from the "beautifulsoup4" ("bs4") package
from bs4 import BeautifulSoup as bs
import requests

#1: Finding the price of an item on Newegg.com, looking for a "$" and finding the subsequent price.
url = "https://www.newegg.com/amd-ryzen-7-5700x-ryzen-7-5000-series/p/N82E16819113735"
result = requests.get(url)
doc = bs(result.text, "html.parser")
prices = doc.find_all(string="$")
parent = prices[0].parent
strong = parent.find("strong")
print(f"1. {strong.string}")

#2: Creating a modified copy of a given HTML file within Python.
with open("venv\Scripts\index.html", "r") as file:
    doc = bs(file, "html.parser")
tags = doc.find_all("h1", type="text")
for tag in tags: #LOOP USED HERE
    tag['placeholder'] = "You have been changed."
with open("venv\Scripts\index.html", "w") as file:
    file.write(str(doc))
print("2. File has been modified!")

#3. Prints the top 10 cryptocurrency prices from CoinMarketCap.com in a dictionary format.
url = "https://coinmarketcap.com/"
result = requests.get(url).text
doc = bs(result, "html.parser")
tbody = doc.tbody
trs = tbody.contents
prices = {} #DICTIONARY USED HERE
for tr in trs[:10]:
    name, price = tr.contents[2:4]
    fixed_name = name.p.string
    fixed_price = price.a.string
    prices[fixed_name] = fixed_price
print(f"3. {prices}")