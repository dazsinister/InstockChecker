import requests
from bs4 import BeautifulSoup
import time
from discord import SyncWebhook

url = "https://www.instocktrades.com/products/mar221128d/captain-marvel-by-kelly-sue-deconnick-omnibus-hc-lopez-var"
url2 = "https://www.instocktrades.com/products/mar221129d/captain-marvel-by-kelly-sue-deconnick-omnibus-hc-mckelvie-dm"
url3 = "https://www.instocktrades.com/products/mar221138d/predator-orig-yrs-omnibus-hc-vol-01-coello-cvr"
url4 = "https://www.instocktrades.com/products/mar221139d/predator-orig-yrs-omnibus-hc-vol-01-warner-dm-var"
url5 = "https://www.instocktrades.com/products/aug227229d/sleeper-omnibus-hc-(2022-edition)-(mr)"
url6 = "https://www.instocktrades.com/products/jul220165d/spawn-origins-dlx-ed-hc-vol-05"


def is_in_stock(url):
    result = requests.get(url)
    doc = BeautifulSoup(result.text, "html.parser")
    cart = doc.find("button", {"class": "btn addtocart"})
    return bool(cart)


while True:
    if is_in_stock(url):
        webhook = SyncWebhook.from_url(
            "https://discord.com/api/webhooks/1052223549563215962/W45EREAJfU7xYI7KJ_v7o6y5FCqDwMaY6DNtZgHGzZWbMmma8Kf5lRYThKflXMSEdKKt")
        webhook.send("Captain Marvel by Kelly Sue Deconnick Omnibus")
        webhook.send(
            "https://www.instocktrades.com/products/mar221128d/captain-marvel-by-kelly-sue-deconnick-omnibus-hc-lopez-var")
        webhook.send("__")

    if is_in_stock(url2):
        webhook = SyncWebhook.from_url(
            "https://discord.com/api/webhooks/1052223549563215962/W45EREAJfU7xYI7KJ_v7o6y5FCqDwMaY6DNtZgHGzZWbMmma8Kf5lRYThKflXMSEdKKt")
        webhook.send("Captain Marvel by Kelly Sue Deconnick Omnibus McKelvie DM Variant")
        webhook.send(
            "https://www.instocktrades.com/products/mar221129d/captain-marvel-by-kelly-sue-deconnick-omnibus-hc-mckelvie-dm")
        webhook.send("__")

    if is_in_stock(url3):
        webhook = SyncWebhook.from_url(
            "https://discord.com/api/webhooks/1052223549563215962/W45EREAJfU7xYI7KJ_v7o6y5FCqDwMaY6DNtZgHGzZWbMmma8Kf5lRYThKflXMSEdKKt")
        webhook.send("Predator Original years Omnibus Volume 01")
        webhook.send(
            "https://www.instocktrades.com/products/mar221138d/predator-orig-yrs-omnibus-hc-vol-01-coello-cvr")
        webhook.send("__")

    if is_in_stock(url4):
        webhook = SyncWebhook.from_url(
            "https://discord.com/api/webhooks/1052223549563215962/W45EREAJfU7xYI7KJ_v7o6y5FCqDwMaY6DNtZgHGzZWbMmma8Kf5lRYThKflXMSEdKKt")
        webhook.send("Predator Original Years Omnibus Volume 01 Warner DM Variant")
        webhook.send(
            "https://www.instocktrades.com/products/mar221139d/predator-orig-yrs-omnibus-hc-vol-01-warner-dm-var")
        webhook.send("__")

    if is_in_stock(url5):
        webhook = SyncWebhook.from_url(
            "https://discord.com/api/webhooks/1052223549563215962/W45EREAJfU7xYI7KJ_v7o6y5FCqDwMaY6DNtZgHGzZWbMmma8Kf5lRYThKflXMSEdKKt")
        webhook.send("Sleeper Omnibus 2022 edition")
        webhook.send(
            "https://www.instocktrades.com/products/aug227229d/sleeper-omnibus-hc-(2022-edition)-(mr)")
        webhook.send("__")

    if is_in_stock(url6):
        webhook = SyncWebhook.from_url(
            "https://discord.com/api/webhooks/1052223549563215962/W45EREAJfU7xYI7KJ_v7o6y5FCqDwMaY6DNtZgHGzZWbMmma8Kf5lRYThKflXMSEdKKt")
        webhook.send("Spawn Origins Deluxe Edition volume 05")
        webhook.send(
            "https://www.instocktrades.com/products/jul220165d/spawn-origins-dlx-ed-hc-vol-05")
        webhook.send("__")

    time.sleep(0)
