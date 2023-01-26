#importing config, data
from data.config import *
from data.data import *
import time
import datetime
from discord import SyncWebhook
import smtplib
from email.mime.text import MIMEText
import logging

urls = [url1, url2, url3, url4, url5, url6, url7, url8, url9, url10]

logging.basicConfig(filename="webhook_data.log", level=logging.DEBUG)

# Function to send an email
def send_email(subject, msg):
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(send, password)
        message = MIMEText(msg)
        message['Subject'] = subject
        message['From'] = send
        message['To'] = receive
        server.sendmail(receive, receive, message.as_string())
        server.quit()
        print("Success: Email sent!")
    except Exception as e:
        print("Email failed to send.")
        print(e)

# damage checking
def is_in_stock(url):
    try:
        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")
        cart = doc.find("button", {"class": "btn addtocart"})
        return bool(cart)
    except Exception as e:
        send_email("Error: exception occured", str(e))
        return False


reported_urls = set()  # set to store URLs that have been reported as in stock

def process_url(url):
    try:
        if url in reported_urls:
            return  # skip the rest of the function if the URL has already been reported

        if is_in_stock(url):
            # code to send the URL to discord
            reported_urls.add(url)
            title = get_title_price(url)
            price = get_title_price(url, get_title=False)
            webhook = SyncWebhook.from_url(link)
            webhook.send(title.text.strip())
            webhook.send(url)
            webhook.send(price.text.strip())
            webhook.send("__")
            send_email("Book instock: " + title.text.strip(),
                       "Title: " + title.text.strip() + "\nURL: " + url + "\nPrice: " + price.text.strip())
            with open('webhook_data.txt', 'a') as f:
                now = datetime.datetime.now()
                timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
                f.write(timestamp + '\n')
                f.write(title.text.strip() + '\n')
                f.write(url + '\n')
                f.write(price.text.strip() + '\n')
                f.write("__\n")
            logging.info("Data sent to webhook and written to file")
    except Exception as e:
        send_email("Error: exception occured", str(e))
        logging.error("Error occurred: " + str(e))

while True:
    current_time = datetime.datetime.now().time()
    start_time = datetime.time(1, 0)
    end_time = datetime.time(23, 0)
    if start_time <= current_time <= end_time:
        for url in urls:
            process_url(url)
        time.sleep(0)
