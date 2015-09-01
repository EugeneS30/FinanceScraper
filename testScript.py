from yahoo.scrape import *

data = getDataBySymbol("MSFT")
print data.getNextEarnDate()