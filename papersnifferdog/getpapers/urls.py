from django.urls import path, re_path
from .views import homePageView, empresas

urlpatterns = [
    path('', homePageView, name='index'),
    path(r'^(?P<paper>\w{5,6})/$', empresas, name='empresas'),
]
