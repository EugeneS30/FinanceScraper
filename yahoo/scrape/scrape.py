from yahoo.containers.data import Data

__author__ = 'eugene.shragovich'

if __name__ == '__main__':
    if __package__ is None:
        import sys
        from os import path
        sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
        from containers.data import Data
    else:
        from ..containers.data import Data

from lxml import html
from bs4 import BeautifulSoup
from urllib2 import urlopen
#from ..containers.data import Data

BASE_URL = "https://finance.yahoo.com"

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

    #return Data(el[])

    return  elementsDict

getDataBySymbol("MSFT", verbose=True)