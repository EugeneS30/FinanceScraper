__author__ = 'eugene.shragovich'

from stockData import StockData

from Config import *

from urllib2 import urlopen
from bs4 import BeautifulSoup

def getDataBySymbol(symbol, verbose=False):
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

        if verbose == True:
            print ("Value: %s, Key: %s") %(key, value)

    return StockData(elementsDict.get("Prev Close"), elementsDict.get("Avg Vol (3m)"), elementsDict.get("Bid"),
                    elementsDict.get("52wk Range"), elementsDict.get("P/E (ttm)"), elementsDict.get("Volume"),
                    elementsDict.get("Day's Range"), elementsDict.get("Beta"), elementsDict.get("1y Target Est"),
                    elementsDict.get("Ask"), elementsDict.get("EPS (ttm)"), elementsDict.get("Open"),
                    elementsDict.get("Market Cap"),elementsDict.get("Next Earnings Date"), elementsDict.get("Div & Yield"))

# data = getDataBySymbol("MSFT")
# print data