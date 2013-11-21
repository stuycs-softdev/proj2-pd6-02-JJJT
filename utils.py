import json
import urllib2

def init(symb):
    url = "http://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20yahoo.finance.quotes%20where%20symbol%20in%20%28%22YHOO%22%29%0A%09%09&env=http%3A%2F%2Fdatatables.org%2Falltables.env&format=json"
    replaced = url.replace("YHOO", symb)
    request = urllib2.urlopen(replaced)
    result = request.read()
    d = json.loads(result)
    return d

def getAsk(symb):
    d = init(symb)
    return d["query"]["results"]["quote"]["Ask"]

def getDailyHigh(symb):
    d = init(symb)
    return d["query"]["results"]["quote"]["DaysHigh"]

def getDailyLow(symb):
    d = init(symb)
    return d["query"]["results"]["quote"]["DaysLow"]

def getPercentChange(symb):
    d = init(symb)
    return d["query"]["results"]["quote"]["ChangeinPercent"]

def getName(symb):
    d = init(symb)
    return d["query"]["results"]["quote"]["Name"]

def getChange(symb):
    d = init(symb)
    return d["query"]["results"]["quote"]["Change"]

def getYearLow(symb):
    d = init(symb)
    return d["query"]["results"]["quote"]["YearLow"]

def getYearHigh(symb):
    d = init(symb)
    return d["query"]["results"]["quote"]["YearHigh"]

def getOpen(symb):
    d = init(symb)
    return d["query"]["results"]["quote"]["Open"]

def getPrevClose(symb):
    d = init(symb)
    return d["query"]["results"]["quote"]["PreviousClose"]

def getOneYearTargetPrice(symb):
    d = init(symb)
    return d["query"]["results"]["quote"]["OneyrTargetPrice"]
