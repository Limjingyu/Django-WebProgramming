from django.urls import path

from enterprise.views import EnterpriseLV

app_name = 'ent'

urlpatterns = [
    # path('list/', EnterpriseLV.as_view(), name='ent_list'),
    path('request_list/', EnterpriseLV.as_view(), name='ent_request_list'),
]
