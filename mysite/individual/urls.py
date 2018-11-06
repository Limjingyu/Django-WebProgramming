from django.urls import path
from individual.views import *
from mysite.views import HomeView


app_name = 'indi'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('request_add', individualCreateView.as_view(), name='request_add'),
]
