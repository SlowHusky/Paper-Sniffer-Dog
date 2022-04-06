from django.core.mail import send_mail

def dogsnifferSendMail(mensagem):
    send_mail(
        'Teste de e-mail',
        mensagem,
        'papersniffer@papersniffer.com',
        ['cliente@cliente.com']
    )



def gain(open_price, now):
    marge = ((100*now)/open_price)-100
    return abs(marge)


def decision(change, paper):
    if change > 1.10:
        print(f'Subiu muito, hold {paper}')
        mensagem = f'Subiu muito, hold {paper}'
        dogsnifferSendMail(mensagem)
    elif 1.05< change <= 1.10:
        print(f'Subiu, sell {paper}')
        mensagem = f'Subiu, sell {paper}'
        dogsnifferSendMail(mensagem)
    elif 0.92 < change <= 0.95:
        print(f'Queda acentuada, aguarde {paper}')
        mensagem = f'Queda acentuada, aguarde {paper}'
        dogsnifferSendMail(mensagem)
    elif change <= 0.92:
        print(f'Caiu muito, compra {paper}')
        mensagem = f'Caiu muito, compra {paper}'
        dogsnifferSendMail(mensagem)
    else:
        print('Nenhuma ação sugerida')