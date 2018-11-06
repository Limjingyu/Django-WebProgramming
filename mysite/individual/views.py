from django.shortcuts import render
from individual.models import individual
# Create your views here.
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from mysite.views import LoginRequiredMixin

class individualCreateView(LoginRequiredMixin, CreateView):
    model = individual
    fields = ['user_name', 'enterprise_name', 'additional']
    success_url = reverse_lazy('indi:home')
    def form_valid(self, form):
        print(form)
        form.instance.owner = self.request.user
        return super(individualCreateView, self).form_valid(form)
