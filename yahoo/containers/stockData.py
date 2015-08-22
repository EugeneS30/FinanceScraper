__author__ = 'Polar'


class StockData(object):

    def __init__(self, prevClose, avgVolume, bid, fiftyTwoWeekRange, PEttm, volume, daysRange, beta, OneYTargetEst, ask,
                 EPSttm, openValue, marketCap, nextEarnDate, DivYield):

        self.prevClose = prevClose
        self.avgVolume = avgVolume
        self.bid = bid
        self.fiftyTwoWeekRange = fiftyTwoWeekRange
        self.PEttm = PEttm
        self.volume = volume
        self.daysRange = daysRange
        self.beta = beta
        self.OneYTargetEst = OneYTargetEst
        self.ask = ask
        self.EPSttm = EPSttm
        self.openValue = openValue
        self.marketCap = marketCap
        self.nextEarnDate = nextEarnDate
        self.DivYield = DivYield

    def __str__(self):

        returnDict = {}

        for key, value in self.__dict__.iteritems():
            returnDict[key] = getattr(self, key)

        return str(returnDict)

    def getPrevClose(self):
        return self.prevClose

    def getAvgVolume(self):
        return self.avgVolume

    def getBid(self):
        return self.bid

    def getFiftyTwoWeekRange(self):
        return self.fiftyTwoWeekRange

    def getPEttm(self):
        return self.PEttm

    def getVolume(self):
        return self.volume

    def getDaysRange(self):
        return self.daysRange

    def getBeta(self):
        return self.beta

    def getOneYTargetEst(self):
        return self.OneYTargetEst

    def getAsk(self):
        return self.ask

    def getEPSttm(self):
        return self.EPSttm

    def getOpen(self):
        return self.openValue

    def getMarketCap(self):
        return self.marketCap

    def getNextEarnDate(self):
        return self.nextEarnDate

    def getDivYield(self):
        return self.DivYield