__author__ = 'Polar'

if __name__ == '__main__':
    if __package__ is None:
        sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
    else:
        from ..yahoo.scrape.scrape import *

data = getDataBySymbol("MSFT")
print data