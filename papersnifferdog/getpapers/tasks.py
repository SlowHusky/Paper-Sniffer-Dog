from celery import Celery
from celery.schedules import crontab
from celery import shared_task
from .manipulations import getAllMonitoring, getPriceFromPaper

app = Celery()
#versão de teste

@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):

    sender.add_periodic_task(
        crontab(minute="*"),
        verify_tunnel(),
    )
@app.task
def verify_tunnel():
    print("start")
    papers = getAllMonitoring()
    for paper in papers:
        item = getPriceFromPaper(paper)
        if item[0].price_now <= (item[0].open_price+item[0].open_price*0.1):
            print(f'Vender {{paper}}')
        else:
            print('Nada!')

