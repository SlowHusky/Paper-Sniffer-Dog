from yahooquery import Ticker
from datetime import datetime

def showAllPapers(acoes):
    for x in acoes:
        item = Ticker(x)
        data = item.history(period="1d")

def showOnePaper(acao):
    item = Ticker(acao)
    data = item.history(period="1d")
    return data

def showBalancePaper(acao):
    item = Ticker(acao)
    return item.summary_detail