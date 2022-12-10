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
    url = "https://www.instocktrades.com/products/mar180976d/spider-man-vs-venom-omnibus-hc"
    phrase = "Not Available"
    available = check_availability(url, phrase)

    if available:
        print('Spider-Man vs Venom')
    else:
        url = "https://www.instocktrades.com/products/may170936d/spider-man-clone-saga-omnibus-hc-vol-02"
        phrase = "Not Available"
        available = check_availability(url, phrase)

        if available:
            print('Clone Saga Volume 2')
        else:
            url = "https://www.instocktrades.com/products/dec181029d/hulk-by-loeb-mcguinness-omnibus-hc"
            phrase = "Not Available"
            available = check_availability(url, phrase)

            if available:
                print('Test')
            else:
                url = "https://www.instocktrades.com/products/oct160998d/war-of-kings-prelude-hc-road-to-war-of-kings-omnibus"
                phrase = "Not Available"
                available = check_availability(url, phrase)

                if available:
                    print('trying to test')
                else:
                    print('Nothing in stock')

    time.sleep(10)  # Wait N minutes to check again.


if __name__ == '__main__':
    main()
