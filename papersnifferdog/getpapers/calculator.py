from email import message
from django.core.mail import send_mail
from .manipulations import insertLogs
from django.utils import timezone

def dogsnifferSendMail(text):
    send_mail(
        'Teste de e-mail',
        text,
        'papersniffer@papersniffer.com',
        ['cliente@cliente.com']
    )



def gain(open_price, now):
    marge = ((100*now)/open_price)-100
    return abs(marge)


def decision(change, paper):
    hour = timezone.now()
    if change > 1.10:
        print(f'Subida muito alta do ativo monitorado, aguarde para vender o ativo {paper}')
        mensagem = str(hour.strftime("%Y-%m-%d %H:%M:%S")) + f' Subida muito alta do ativo monitorado, aguarde para vender o ativo {paper}'
        insertLogs(mensagem)
        dogsnifferSendMail(mensagem)
    elif 1.05< change <= 1.10:
        print(f'Subida considerável do ativo monitorado, considere vender o ativo {paper}')
        mensagem = str(hour.strftime("%Y-%m-%d %H:%M:%S")) + f' Subida considerável do ativo monitorado, considere vender o ativo {paper}'
        dogsnifferSendMail(mensagem)
    elif 0.92 < change <= 0.95:
        print(f'Queda acentuada do ativo monitorado, considere aguardar para vender o ativo {paper}')
        mensagem = str(hour.strftime("%Y-%m-%d %H:%M:%S")) + f' Queda acentuada do ativo monitorado, aguarde para vender o ativo {paper}'
        insertLogs(mensagem)
        dogsnifferSendMail(mensagem)
    elif change <= 0.92:
        print(f'Queda do ativo monitorado, considere a compra do ativo {paper}')
        mensagem = str(hour.strftime("%Y-%m-%d %H:%M:%S")) + f' Queda do ativo monitorado, considere a compra do ativo {paper}'
        insertLogs(mensagem)
        dogsnifferSendMail(mensagem)
    else:
        print('Nenhuma ação sugerida')