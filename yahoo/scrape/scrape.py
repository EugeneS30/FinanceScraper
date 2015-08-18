__author__ = 'eugene.shragovich'

from lxml import html
from bs4 import BeautifulSoup
from urllib2 import urlopen

BASE_URL = "https://finance.yahoo.com"

def getDataBySymbol(symbol):
    symbolPart = "/q?s=%s" %symbol

    actualURL = BASE_URL + symbolPart
    htmlContent = urlopen(actualURL).read()

    soup = BeautifulSoup(htmlContent, "lxml")
    data = soup.find("div", "rtq_table")

    elements = [tr.getText() for tr in data.findAll("tr")]

    elementsDict = {}


    for el in elements:
        key = el.split(":")[0]
        value = el.split(":")[1]
        elementsDict[key] = value

    return  elementsDict
