from django.urls import path
from django.conf.urls import url
from enterprise.views import EnterpriseRLV, EnterpriseALV

app_name = 'ent'

urlpatterns = [
    # path('list/', EnterpriseLV.as_view(), name='ent_list'),
    path('request_list', EnterpriseRLV.as_view(), name='request_list'),
    path('approve_list', EnterpriseALV.as_view(), name= 'approve_list')
]
