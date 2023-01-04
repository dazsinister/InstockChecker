
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

def header4():
    result = requests.get(url4)
    doc = BeautifulSoup(result.text, "html.parser")
    title4 = doc.find("h1")
    return title4

def header5():
    result = requests.get(url5)
    doc = BeautifulSoup(result.text, "html.parser")
    title5 = doc.find("h1")
    return title5

def header6():
    result = requests.get(url6)
    doc = BeautifulSoup(result.text, "html.parser")
    title6 = doc.find("h1")
    return title6

def header7():
    result = requests.get(url7)
    doc = BeautifulSoup(result.text, "html.parser")
    title7 = doc.find("h1")
    return title7

def header8():
    result = requests.get(url8)
    doc = BeautifulSoup(result.text, "html.parser")
    title8 = doc.find("h1")
    return title8

title1 = header1()
title2 = header2()
title3 = header3()
title4 = header4()
title5 = header5()
title6 = header6()
title7 = header7()
title8 = header8()
