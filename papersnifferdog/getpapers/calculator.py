def gain(open_price, now):
    marge = ((100*now)/open_price)-100
    return abs(marge)


def decision(change):
    if change > 1.10:
        print('Subiu muito, hold')
    elif 1.05< change <= 1.10:
        print('Subiu, sell')
    elif 0.92 < change <= 0.95:
        print('Queda acentuada, aguarde')
    elif change <= 0.92:
        print('Caiu muito, compra')
    else:
        print('Nenhuma ação sugerida')