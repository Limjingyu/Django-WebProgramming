from django.shortcuts import render
from django.views.generic import ListView

from enterprise.models import ApplyBuffer, BlockChain

# Create your views here.
class EnterpriseRLV(ListView):
    model = ApplyBuffer

class EnterpriseALV(ListView):
    model = BlockChain