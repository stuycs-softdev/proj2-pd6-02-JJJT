import json
import urllib2

def init(symb):
    url = "http://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20yahoo.finance.quotes%20where%20symbol%20in%20%28%22YHOO%22%29%0A%09%09&env=http%3A%2F%2Fdatatables.org%2Falltables.env&format=json"
    replaced = url.replace("YHOO", symb)
    request = urllib2.urlopen(replaced)
    result = request.read()
    d = json.loads(result)
    quote = d["query"]["results"]["quote"]
    asdf = {}
    asdf['ask'] = quote['Ask']
    asdf['dHigh'] = quote['DaysHigh']
    asdf['dLow'] = quote['DaysLow']
    asdf['pChange'] = quote['ChangeInPercent']
    asdf['name'] = quote['Name']
    asdf['change'] = quote['Change']
    asdf['yLow'] = quote['YearLow']
    asdf['yHigh'] = quote['YearHigh']
    asdf['open'] = quote['Open']
    asdf['close'] = quote['PreviousClose']
    asdf['target'] = quote['OneyrTargetPrice']
    return asdf

