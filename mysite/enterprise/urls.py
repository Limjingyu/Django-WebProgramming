from django.urls import path
from django.conf.urls import url
from enterprise.views import *

app_name = 'ent1'

urlpatterns = [
   
    # path('request_list', EnterpriseLV.as_view(), name='request_list'),
    path('request_li', EnterpriseLV.as_view(), name='request_list'),
]
