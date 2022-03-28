from django.urls import path, re_path
from .views import homePageView, empresas, monitor

urlpatterns = [
    path('', homePageView, name='index'),
    re_path(r'^empresas/(?P<paper>.{5,9})/', empresas, name='empresas'),
    path('monitor', monitor, name='monitor' ),
]
