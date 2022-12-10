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
                    print('trying to test')
                else:
                    print('Nothing in stock')

    time.sleep(10)  # Wait N minutes to check again.


if __name__ == '__main__':
    main()
