from django.contrib import admin
from enterprise.models import ApplyBuffer

# Register your models here.
class EnterpriseAdmin(admin.ModelAdmin):
    list_display = ('individual_id', 'ent_id', 'request_date',)
    list_filter = ('request_date',)

admin.site.register(ApplyBuffer, EnterpriseAdmin)
