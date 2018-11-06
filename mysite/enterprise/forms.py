from django import forms
# from .models import InputForm


# class InputForm(forms.ModelForm):
    
#     name_indi                   = forms.CharField(max_length=50)
#     social_id                   = forms.CharField(max_length=50)
#     address_indi                = forms.CharField(max_length=50)
#     name_enterprise             = forms.CharField(max_length=50)
#     Business_license_number     = forms.CharField(max_length=50)     
#     representative_name         = forms.CharField(max_length=50)
#     industry                    = forms.CharField(max_length=50)
#     address_ent                 = forms.CharField(max_length=100)
#     department                  = forms.CharField(max_length=50)
#     position                    = forms.CharField(max_length=50)
#     assigned_task               = forms.CharField(max_length=50)
#     content                     = forms.TextField('CONTENT')
#     working_period              = forms.CharField(max_length=100)
#     department_a                = forms.CharField(max_length=50)
#     name_a                      = forms.CharField(max_length=50)
#     position_a                  = forms.CharField(max_length=50)
#     contact_number_a            = forms.CharField(max_length=50)
#     purpose                     = forms.CharField(max_length=50)
#     class Meta:
#         model = InputForm
#         fields=('name_indi', 'social_id', 'address_indi', 'name_enterprise', 'Business_license_number',
#                  'representative_name', 'industry', 'address_ent', 'department', 'position', 'assigned_task',
#                   'content', 'working_period', 'department_a', 'name_a', 'position_a', 'contact_number_a',
#                    'purpose', 'create_date',)
