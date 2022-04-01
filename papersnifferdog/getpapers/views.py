from datetime import datetime, time, date
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.utils import timezone
from .getdata import showAllPapers, showOnePaper, showBalancePaper, returnTicker
from .models import Papers, Prices, Monitoring
from .manipulations import getAllDataPapers, getPriceFromPaper, getAllMonitoring, getMonitoredSymbols


acoes = ["ABCB4.SA", "ALPA4.SA", "ALUP11.SA", "ABEV3.SA", "ANIM3.SA", "ARZZ3.SA",
        "AZUL4.SA", "B3SA3.SA", "BRSR6.SA", "BBSE3.SA", "BKBR3.SA", "BRML3.SA",
        "BRPR3.SA", "BBDC3.SA", "BBDC4.SA", "BRAP4.SA", "BBAS3.SA", "BRKM5.SA",
        "BRFS3.SA", "BPAC11.SA", "CAML3.SA", "CRFB3.SA", "CCRO3.SA", "CMIG3.SA",
        "CMIG4.SA", "CIEL3.SA", "CGAS5.SA", "CSMG3.SA", "CPLE6.SA",
        "CSAN3.SA",  "CPFE3.SA", "CVCB3.SA", "CYRE3.SA", "DIRR3.SA",
        "DMMO3.SA", "ECOR3.SA", "ELET3.SA", "ELET6.SA", "EMBR3.SA", "ENBR3.SA",
        "ENGI11.SA", "ENEV3.SA", "EGIE3.SA", "EQTL3.SA", "EVEN3.SA", "EZTC3.SA",
        "FESA4.SA", "FLRY3.SA", "GFSA3.SA", "GGBR4.SA", "GOAU4.SA", "GOLL4.SA",
        "GRND3.SA", "GUAR3.SA", "HAPV3.SA", "HBOR3.SA", "HYPE3.SA", "PARD3.SA",
        "MEAL3.SA", "MYPK3.SA", "IRBR3.SA", "ITSA4.SA", "ITUB3.SA", "ITUB4.SA",
        "JBSS3.SA", "KLBN11.SA", "LIGT3.SA", "RENT3.SA", "AMAR3.SA", "LREN3.SA",
        "MDIA3.SA", "MGLU3.SA", "POMO4.SA", "MRFG3.SA", "LEVE3.SA", "BEEF3.SA",
        "MOVI3.SA", "MRVE3.SA", "MULT3.SA", "ODPV3.SA", "PETR3.SA",
        "PETR4.SA", "PRIO3.SA", "PSSA3.SA", "PTBL3.SA", "QUAL3.SA", "RADL3.SA",
        "RAPT4.SA", "RAIL3.SA", "SBSP3.SA", "SAPR11.SA", "SANB11.SA", "STBP3.SA",
        "SMTO3.SA", "SEER3.SA", "CSNA3.SA", "SLCE3.SA", "SULA11.SA", "SUZB3.SA",
        "TAEE11.SA", "TGMA3.SA", "TOTS3.SA", "TRPL4.SA", "TUPY3.SA", "UGPA3.SA",
        "UNIP6.SA", "USIM5.SA", "VALE3.SA", "VLID3.SA", "VULC3.SA", "WEGE3.SA",
        "WIZS3.SA", "VIVA3.SA", "CEAB3.SA", "YDUQ3.SA", "COGN3.SA", "BIDI11.SA",
        "BIOM3.SA", "BPAN4.SA", "CARD3.SA", "FHER3.SA", "FRAS3.SA",
        "FRTA3.SA", "GPIV33.SA", "LPSB3.SA", "LOGN3.SA", 
        "MILS3.SA", "OFSA3.SA", "OIBR3.SA", "PFRM3.SA", "ROMI3.SA",
        "PMAM3.SA", "RSID3.SA", "SCAR3.SA", "SGPS3.SA", "SHOW3.SA", "SLED3.SA",
        "TCSA3.SA", "TECN3.SA", "TELB4.SA", "TEND3.SA", "TPIS3.SA",
        "TRIS3.SA", "VIVR3.SA", "NTCO3.SA", "PCAR3.SA"]


def homePageView(request):
    data_papers = []
    a = getAllDataPapers()
    for x in a:
        b = getPriceFromPaper(x.symbol)
        data_papers.append((x.title, x.symbol, b[0].price_now, b[0].ask, b[0].bid, b[0].open_price, b[0].date_info))
    context = {
        'data_papers': data_papers,
    }
    template = loader.get_template('getpapers/index.html')
    return HttpResponse(template.render(context, request))

def monitor(request):
    if request.method == "GET":
        list_monitored = getMonitoredSymbols()
        data_name = []
        names = []
        a = getAllDataPapers()
        for x in a:
            data_name.append(x.symbol)
            names.append(x.title)
        print(list_monitored)
        context = {
            'data_name': data_name,
            'monitored': list_monitored,
            'names': names,
        }
        template = loader.get_template('getpapers/formulario.html')
        return HttpResponse(template.render(context, request))
    else:
        form = request.POST
        print(form)
        return HttpResponse("POST RECEBIDO!")

def empresas(request,paper):
    info = showBalancePaper(paper)
    info = info[paper]
    print(info['regularMarketDayLow'])
    context ={
        'paper':paper,
        'info': info,
    }
    template = loader.get_template('getpapers/empresas.html')
    return HttpResponse(template.render(context, request))

def firstExec(request):
    for x in acoes:
        a = returnTicker(x)
        b = a.financial_data
        c = a.asset_profile
        d = a.price
        a = a.summary_detail
        query1 = Papers(symbol = x, description = c[x]['longBusinessSummary'], title = d[x]['longName'])
        query1.save()

        query2 = Prices(paper = query1, date_info = timezone.now(), price_now = b[x]['currentPrice'], ask = a[x]['ask'], bid =  a[x]['bid'],
        high_price = a[x]['dayHigh'], low_price = a[x]['dayLow'], open_price = a[x]['open'], estimated_close_price = a[x]['previousClose'],
        volume = a[x]['volume'])  
        query2.save()
    return HttpResponse("Finished")
