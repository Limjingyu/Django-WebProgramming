from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ApplyBuffer(models.Model):
    request_date = models.DateTimeField('Request Date', auto_now=True)
    indi_id = models.ForeignKey(User, related_name='individual_id', null=False, on_delete=models.CASCADE)
    ent_id = models.ForeignKey(User, related_name='enterprise_id', null=False, on_delete=models.CASCADE)

class BlockChain(models.Model):
    pass