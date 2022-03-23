from django.db import models

# Create your models here.
class Papers(models.Model):
    title = models.CharField(max_length=100)
    symbol = models.CharField(max_length=10)

    description = models.TextField(("Description here"))

    def __str__(self):
        return self.title

class Prices(models.Model):
    paper = models.ForeignKey(Papers, on_delete=models.CASCADE)
    date_info = models.DateTimeField('date collected')
    low_price = models.FloatField()
    high_price = models.FloatField()
    open_price = models.FloatField()
    close_price = models.FloatField()
    volume = models.FloatField()
    adjclose = models.FloatField()