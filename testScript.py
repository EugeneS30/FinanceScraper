import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )


from yahoo.scrape import *

data = getDataBySymbol("MSFT")
print data