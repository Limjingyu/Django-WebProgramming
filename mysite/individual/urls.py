from django.urls import path
from individual.views import *

app_name = 'indi'

urlpatterns = [
    path('request_add', individualCreateView.as_view(), name='request_add'),
]
