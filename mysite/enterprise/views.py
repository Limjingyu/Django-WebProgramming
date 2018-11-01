from django.shortcuts import render
from django.views.generic import ListView

from enterprise.models import ApplyBuffer

# Create your views here.
class EnterpriseLV(ListView):
    model = ApplyBuffer