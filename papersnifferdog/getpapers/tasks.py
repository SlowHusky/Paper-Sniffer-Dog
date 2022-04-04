from celery import Celery
from celery.schedules import crontab
from celery import periodic_task
from .manipulations import getAllMonitoring, getPriceFromPaper

@periodic_task(
    run_every=(crontab(minute='*')),
    name="verify_tunnel",
    ignore_result=True
)

@periodic_task
def verify_tunnel():
    print('ok')
    papers = getAllMonitoring()
    for paper in papers:
        item = getPriceFromPaper(paper)
        if item[0].price_now <= (item[0].open_price+item[0].open_price*0.1):
            print(f'Vender {{paper}}')
        else:
            print('Nada!')

