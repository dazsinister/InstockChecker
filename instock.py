import requests
from bs4 import BeautifulSoup
from name import *
from price import *
import time
from discord import SyncWebhook
from config import *

# damage checking
def is_in_stock(url):
    result = requests.get(url)
    doc = BeautifulSoup(result.text, "html.parser")
    cart = doc.find("button", {"class": "btn addtocart"})
    return bool(cart)

while True:
    if is_in_stock(url):
        webhook = SyncWebhook.from_url(link)
        webhook.send(title1.text.strip())
        webhook.send(
            url)
        webhook.send(price1.text.strip())
        webhook.send("__")

    if is_in_stock(url2):
        webhook = SyncWebhook.from_url(link)
        webhook.send(title2.text.strip())
        webhook.send(
            url2)
        webhook.send(price2.text.strip())
        webhook.send("__")
    if is_in_stock(url3):
        webhook = SyncWebhook.from_url(link)
        webhook.send(title3.text.strip())
        webhook.send(
            url3)
        webhook.send(price3.text.strip())
        webhook.send("__")

    if is_in_stock(url4):
        webhook = SyncWebhook.from_url(link)
        webhook.send(title4.text.strip())
        webhook.send(
            url4)
        webhook.send(price4.text.strip())
        webhook.send("__")

    if is_in_stock(url5):
        webhook = SyncWebhook.from_url(link)
        webhook.send(title5.text.strip())
        webhook.send(
            url5)
        webhook.send(price5.text.strip())
        webhook.send("__")

    if is_in_stock(url6):
        webhook = SyncWebhook.from_url(link)
        webhook.send(title6.text.strip())
        webhook.send(
            url6)
        webhook.send(price6.text.strip())
        webhook.send("__")

    if is_in_stock(url7):
        webhook = SyncWebhook.from_url(link)
        webhook.send(title7.text.strip())
        webhook.send(
            url7)
        webhook.send(price7.text.strip())
        webhook.send("__")

    if is_in_stock(url8):
        webhook = SyncWebhook.from_url(link)
        webhook.send(title8.text.strip())
        webhook.send(
            url8)
        webhook.send(price8.text.strip())
        webhook.send("__")

    time.sleep(0)
