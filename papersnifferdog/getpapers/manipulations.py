from .models import Papers, Prices, Monitoring

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