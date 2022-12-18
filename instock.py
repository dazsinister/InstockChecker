import requests
from bs4 import BeautifulSoup
import time
from discord import SyncWebhook

url = "item number 1c"
url2 = "item number 2"


def is_in_stock(url):
    result = requests.get(url)
    doc = BeautifulSoup(result.text, "html.parser")
    cart = doc.find("button", {"class": "btn addtocart"})
    return bool(cart)


while True:
    if is_in_stock(url):
        webhook = SyncWebhook.from_url(
            "discord url")
        webhook.send(
            "message here")
    if is_in_stock(url2):
        webhook = SyncWebhook.from_url(
            "discord url")
        webhook.send(
            "message here")
    time.sleep(10)
