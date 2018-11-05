from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from django.http import HttpResponse

# from enterprise.models import ApplyBuffer

# Create your views here.
class EnterpriseLV(TemplateView):
    # model = ApplyBuffer
    template_name = 'test.html'