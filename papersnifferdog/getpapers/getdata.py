from yahooquery import Ticker
from datetime import datetime

def showAllPapers(acoes):
    for x in acoes:
        item = Ticker(x)
        data = item.history(period="1d")
        print(x, data.open[0], data.close[0],
            data.volume[0], data.high[0],
            data.low[0], data.adjclose[0],
            datetime.now())

def showOnePaper(acao):
    item = Ticker(acao)
    data = item.history(period="1d")
    print(acao, data.open[0], data.close[0],
          data.volume[0], data.high[0],
          data.low[0], data.adjclose[0],
          datetime.now())