from django.shortcuts import render
from django.views.generic import ListView

from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from mysite.views import LoginRequiredMixin

from individual.models import individual
from enterprise.models import ApplyBuffer, BlockChain
# from .forms import InputForm

# Create your views here.
class EnterpriseRLV(LoginRequiredMixin, ListView):
    template_name = 'ent/applybuffer_list.html'

    def get_queryset(self):
        return individual.objects.filter(owner=self.request.user)

class EnterpriseALV(ListView):
    model = BlockChain

# def InputForm(request):
#     if request.method == 'POST': # 폼이 제출되었을 경우...
#         form = ContactForm(request.POST) # 폼은 POST 데이터에 바인드됨
#         if form.is_valid(): # 모든 유효성 검증 규칙을 통과
#             # form.cleaned_data에 있는 데이터를 처리
#             # ...
#             return HttpResponseRedirect('/thanks/') # Redirect after POST
#     else:
#         form = ContactForm() # An unbound form

#     return render_to_response('contact.html', {
#         'form': form,
#     })