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
    