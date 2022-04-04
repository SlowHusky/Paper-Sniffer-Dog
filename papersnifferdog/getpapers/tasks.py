from .manipulations import *
from django.utils import timezone
from .getdata import showAllPapers, showOnePaper, showBalancePaper, returnTicker
from .models import Papers, Prices, Monitoring
from papersnifferdog.celery import app

#tempo configurável, requisito do escopo
app.conf.beat_schedule = {
    'every-10-seconds': {
        'task': 'getpapers.tasks.verify_tunnel',
        'schedule': 60.0,
        'args': (),
    },
    'every-5-minutes': {
        'task': 'getpapers.tasks.update_prices',
        'schedule': 150.0,
        'args': (),
    },
}




@app.task
def verify_tunnel():
    papers = getMonitoredSymbols()
    for paper in papers:
        item = getLatestPriceFromPaper(paper)
        #print(paper,item.price_now)
'''        if item[0].price_now <= (item[0].open_price+item[0].open_price*0.1):
            print(f'Vender {{paper}}')
        else:
            print('Nada!')'''

@app.task
def update_prices():
    list_papers = getAllSymbols()
    for x in list_papers:
            y = getPaperFromSymbol(x)
            a = returnTicker(x)
            b = a.financial_data
            c = a.asset_profile
            d = a.price
            a = a.summary_detail

            query2 = Prices(paper = y, date_info = timezone.now(), price_now = b[y]['currentPrice'], ask = a[y]['ask'], bid =  a[y]['bid'],
            high_price = a[y]['dayHigh'], low_price = a[y]['dayLow'], open_price = a[y]['open'], estimated_close_price = a[y]['previousClose'],
            volume = a[y]['volume'])

            print(query2)
            query2.save()