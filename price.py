import requests
from bs4 import BeautifulSoup
import time
from  config import *

def cost1():
    result = requests.get(url)
    doc = BeautifulSoup(result.text, "html.parser")
    price1 = doc.find("div", {"class": "price"})
    return price1

def cost2():
    result = requests.get(url2)
    doc = BeautifulSoup(result.text, "html.parser")
    price2 = doc.find("div", {"class": "price"})
    return price2

def cost3():
    result = requests.get(url3)
    doc = BeautifulSoup(result.text, "html.parser")
    price3 = doc.find("div", {"class": "price"})
    return price3

def cost4():
    result = requests.get(url4)
    doc = BeautifulSoup(result.text, "html.parser")
    price4 = doc.find("div", {"class": "price"})
    return price4

def cost5():
    result = requests.get(url5)
    doc = BeautifulSoup(result.text, "html.parser")
    price5 = doc.find("div", {"class": "price"})
    return price5

def cost6():
    result = requests.get(url6)
    doc = BeautifulSoup(result.text, "html.parser")
    price6 = doc.find("div", {"class": "price"})
    return price6

def cost7():
    result = requests.get(url7)
    doc = BeautifulSoup(result.text, "html.parser")
    price7 = doc.find("div", {"class": "price"})
    return price7

def cost8():
    result = requests.get(url8)
    doc = BeautifulSoup(result.text, "html.parser")
    price8 = doc.find("div", {"class": "price"})
    return price8

price1 = cost1()
price2 = cost2()
price3 = cost3()
price4 = cost4()
price5 = cost5()
price6 = cost6()
price7 = cost7()
price8 = cost8()
