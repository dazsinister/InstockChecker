import requests
from bs4 import BeautifulSoup
import time
from  config import *

def header1():
    result = requests.get(url)
    doc = BeautifulSoup(result.text, "html.parser")
    title1 = doc.find("h1")
    return title1

def header2():
    result = requests.get(url2)
    doc = BeautifulSoup(result.text, "html.parser")
    title2 = doc.find("h1")
    return title2

def header3():
    result = requests.get(url3)
    doc = BeautifulSoup(result.text, "html.parser")
    title3 = doc.find("h1")
    return title3
