from celery.schedules import crontab
from celery.decorators import task
from celery.utils.log import get_task_logger
from celery.decorators import periodic_task
from .manipulations import getAllMonitoring, getPriceFromPaper

logger = get_task_logger(__name__)



@periodic_task(run_every=(crontab(minute='*/15')), name="some_task", ignore_result=True)
def some_task():
    print("OK!")

#versão de teste
@periodic_task(run_every=(crontab(minute='*/15')), name="verify_tunnel", ignore_result=True)
def verify_tunnel():
    papers = getAllMonitoring()
    for paper in papers:
        item = getPriceFromPaper(paper)
        if item[0].price_now <= (item[0].open_price+item[0].open_price*0.1):
            print(f'Vender {{paper}}')
        else:
            print('Nada!')
        logger.info('action executed')