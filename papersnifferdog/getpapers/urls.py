from django.urls import path, re_path
from .views import homePageView, empresas

urlpatterns = [
    path('', homePageView, name='index'),
    re_path(r'^empresas/(?P<paper>\w{5,6})/', empresas, name='empresas'),
]
