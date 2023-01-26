import requests
from bs4 import BeautifulSoup
from data.config import *

def get_title_price(url, get_title=True):
    try:
        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")
        if get_title:
            return doc.find("h1")
        else:
            return doc.find("div", {"class": "price"})
    except requests.exceptions.RequestException as e:
        print("Error:", e)
    except Exception as e:
        print("Error:", e)

urls = [url1, url2, url3, url4, url5, url6, url7, url8, url9, url10]

for url in urls:
    title = get_title_price(url)
    price = get_title_price(url, get_title=False)
