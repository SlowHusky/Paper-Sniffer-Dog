from django.contrib import admin

from .models import Papers, Prices, Monitoring

# Register your models here.
admin.site.register(Papers)
admin.site.register(Prices)
admin.site.register(Monitoring)