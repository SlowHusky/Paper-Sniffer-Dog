''' Biblioteca para a interagir com o banco de dados,
    sem criar problemas de segurança
    ou manipular querys grandes                      '''


from .models import Papers, Prices, Monitoring, Logmessages

def getAllDataPapers():
    return Papers.objects.all()

def getAllPrices():
    return Prices.objects.all()

def getAllMonitoring():
    return Monitoring.objects.all()

def getPaperFromSymbol(paper):
    return Papers.objects.get(symbol = paper)

def getPriceFromPaper(paper):
    stock = getPaperFromSymbol(paper)
    return Prices.objects.filter(paper=stock)

def getLatestPriceFromPaper(paper):
    stock = getPaperFromSymbol(paper)
    return Prices.objects.filter(paper=stock).latest('date_info')

def getLatest100PriceFromPaper(paper):
    stock = getPaperFromSymbol(paper)
    return Prices.objects.filter(paper=stock).order_by('-id')[:100:-1]

def getMonitoredSymbols():
    monitored =[]
    for x in getAllDataPapers():
        y = x.symbol
        if Monitoring.objects.filter(paper = x):
            monitored.append(y)
    return monitored

def addMonitoredBySymbol(lista):
    Monitoring.objects.all().delete()
    for x in lista:
        a = getPaperFromSymbol(x)
        query = Monitoring(paper = a)
        query.save()
    print("Finnished")

def getAllSymbols():
    papers = []
    for x in getAllDataPapers():
        y = x.symbol
        papers.append(y)
    return papers 

def insertLogs(mensagem):
    query = Logmessages(message = mensagem)
    query.save()

def getLatest100message():
    return Logmessages.objects.all().order_by('-id')[:100]