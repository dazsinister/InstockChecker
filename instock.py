import requests
from bs4 import BeautifulSoup
from config import *
from price import *
from name import *
import time
from discord import SyncWebhook


def is_in_stock(url):
    result = requests.get(url)
    doc = BeautifulSoup(result.text, "html.parser")
    cart = doc.find("button", {"class": "btn addtocart"})
    return bool(cart)


while True:
    if is_in_stock(url):
        webhook = SyncWebhook.from_url(link)
        webhook.send(header1)
        webhook.send(
            url)
        webhook.send(cost1)
        webhook.send("__")
    if is_in_stock(url2):
        webhook = SyncWebhook.from_url(link)
        webhook.send(header2)
        webhook.send(
            url2)
        webhook.send(cost2)
        webhook.send("__")

    time.sleep(0)
