import json
import smtplib
import urllib.request
from datetime import datetime, time
from bs4 import BeautifulSoup

def check_availability(url, phrase):
    global log
    try:
        page = urllib.request.urlopen(url)
        soup = BeautifulSoup(page, features='html.parser')
        if phrase in soup.text:
            return False
        return True
    except:
        log += "Error parsing the website"

def main():
    url = "https://www.website.com"
    phrase = "Not Available"
    available = check_availability(url, phrase)

    if available:
        print('Spider-Man vs Venom')
    else:
        url = "https://www.website.com"
        phrase = "Not Available"
        available = check_availability(url, phrase)

        if available:
            print('Clone Saga Volume 2')
        else:
            url = "https://www.website.com"
            phrase = "Not Available"
            available = check_availability(url, phrase)

            if available:
                print('Test')
            else:
                url = "https://www.website.com"
                phrase = "Not Available"
                available = check_availability(url, phrase)

                if available:
                    print('trying to test')import urllib.request
from bs4 import BeautifulSoup
import time
import requests
from discord import SyncWebhook

with requests.Session() as c:
    url = 'https://www.instocktrades.com/account/login'
    USERNAME = 'josh.mcdermott88@icloud.com'
    PASSWORD = 'Hailey8820'
    c.get(url)
    login_data = dict(username=USERNAME, password=PASSWORD, next='/')
    c.post(url, data=login_data, headers={"Referer": "https://www.instocktrades.com/account/login"})import urllib.request
from bs4 import BeautifulSoup
import time
import requests
from discord import SyncWebhook

with requests.Session() as c:
    url = 'https://www.instocktrades.com/account/login'
    USERNAME = 'username'
    PASSWORD = 'password'
    c.get(url)
    login_data = dict(username=USERNAME, password=PASSWORD, next='/')
    c.post(url, data=login_data, headers={"Referer": "https://www.instocktrades.com/account/login"})

def check_availability(url, phrase):
    global log
    try:
        page = urllib.request.urlopen(url)
        soup = BeautifulSoup(page, features='html.parser')
        if phrase in soup.text:
            return False
        return True
    except:
        log += "Error parsing the website"

def main():
    url = "https://www.website"
    phrase = "Not Available"
    not_available = check_availability(url, phrase)

    while (not_available) == False:
        print('Out of Stock')
        time.sleep(60*5)
    else:
        webhook = SyncWebhook.from_url("https://discord.com/api/webhooks/1052223549563215962/W45EREAJfU7xYI7KJ_v7o6y5FCqDwMaY6DNtZgHGzZWbMmma8Kf5lRYThKflXMSEdKKt")
        webhook.send("https://www.instocktrades.com/products/jul220080/ascender-dlx-ed-hc-(mr)")

if __name__ == '__main__':
    main(

def check_availability(url, phrase):
    global log
    try:
        page = urllib.request.urlopen(url)
        soup = BeautifulSoup(page, features='html.parser')
        if phrase in soup.text:
            return False
        return True
    except:
        log += "Error parsing the website"

def main():
    url = "https://www.instocktrades.com/products/JAN221037/spider-man-clone-saga-omnibus-hc-vol-02"
    phrase = "Not Available"
    not_available = check_availability(url, phrase)

    while (not_available) == False:
        print('Out of Stock')
        time.sleep(60*5)
    else:
        webhook = SyncWebhook.from_url("https://discord.com/api/webhooks/1052223549563215962/W45EREAJfU7xYI7KJ_v7o6y5FCqDwMaY6DNtZgHGzZWbMmma8Kf5lRYThKflXMSEdKKt")
        webhook.send("https://www.instocktrades.com/products/jul220080/ascender-dlx-ed-hc-(mr)")

if __name__ == '__main__':
    main(
                else:
                    print('Nothing in stock')

    time.sleep(10)  # Wait N minutes to check again.


if __name__ == '__main__':
    main()
