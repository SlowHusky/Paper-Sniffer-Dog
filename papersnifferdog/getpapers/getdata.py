'''
    Biblioteca para a manipulação das ações
    da api do yahooquery
'''

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

def returnTicker(acao):
    item = Ticker(acao)
    return item

def showPaperinformations(acao):
    item =  returnTicker(acao)
    item = item.asset_profile
    item = item[acao]
    return item
