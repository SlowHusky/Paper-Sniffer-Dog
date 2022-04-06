from distutils.log import error
from .manipulations import *
from django.utils import timezone
from .getdata import showAllPapers, showOnePaper, showBalancePaper, returnTicker
from .models import Papers, Prices, Monitoring
from papersnifferdog.celery import app
from .calculator import gain, decision
#teste
from django.core.mail import send_mail

#tempo configurável, requisito do escopo
app.conf.beat_schedule = {
    'every-15-minutes': {
        'task': 'getpapers.tasks.verify_tunnel',
        'schedule': 600.0,
        'args': (),
    },
    'every-5-minutes': {
        'task': 'getpapers.tasks.update_prices',
        'schedule': 300.0,
        'args': (),
    },
}


#Tunel de preços
@app.task
def verify_tunnel():
    papers = getMonitoredSymbols()

    for paper in papers:
        item = getLatestPriceFromPaper(paper)
        print(f'abriu: {item.open_price} agora: {item.price_now}')
        if item.open_price > 0:
            change = item.price_now/item.open_price
            decision(change, paper)
        else:
            print('Mercado fechado')


@app.task
def update_prices():
    list_papers = getAllSymbols()
    for x in list_papers:
            y = getPaperFromSymbol(x)
            a = returnTicker(x)
            b = a.financial_data
            a = a.summary_detail

            query2 = Prices(paper = y, date_info = timezone.now(), price_now = b[x]['currentPrice'], ask = a[x]['ask'], bid =  a[x]['bid'],
            high_price = a[x]['dayHigh'], low_price = a[x]['dayLow'], open_price = a[x]['open'], estimated_close_price = a[x]['previousClose'],
            volume = a[x]['volume'])
            try:
                query2.save()
                print('Query saved')
            except error:
                print(query2)