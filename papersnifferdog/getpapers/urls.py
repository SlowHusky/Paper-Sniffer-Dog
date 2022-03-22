from django.urls import path
from .views import homePageView

urlpatterns = [
    path('', homePageView.as_view(), name='index'),
]
