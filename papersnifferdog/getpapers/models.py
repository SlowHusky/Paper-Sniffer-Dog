from django.db import models


# Create your models here.
class Papers(models.Model):
    title = models.CharField(max_length=100)
    symbol = models.CharField(max_length=10)

    description = models.TextField(("Description here"))

    def __str__(self):
        return self.symbol

class Prices(models.Model):
    paper = models.ForeignKey(Papers, on_delete=models.CASCADE)
    date_info = models.DateTimeField('date published')
    price_now = models.FloatField()
    ask = models.FloatField()
    bid = models.FloatField()
    low_price = models.FloatField()
    high_price = models.FloatField()
    open_price = models.FloatField()
    estimated_close_price = models.FloatField()
    volume = models.FloatField()

class Monitoring(models.Model):
    paper = models.ForeignKey(Papers, on_delete=models.CASCADE)
    total_alerts = models.IntegerField(default=0)