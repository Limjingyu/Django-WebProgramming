from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.
class individual(models.Model):
    user_name = models.CharField('USER_NAME', max_length = 50)
    enterprise_name = models.CharField('ENTERPRISE_NAME', max_length = 50)
    additional = models.TextField('ADDITIONAL')
    create_date = models.DateTimeField('Create Date', auto_now_add=True)
    Modify_date = models.DateTimeField('Modify Date', auto_now= True)
    owner = models.ForeignKey(User, null= True, on_delete=models.CASCADE)

    def get_next_post(self):
        return self.get_next_by_modify_date()

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title, allow_unicode= True)
        super(individual,self).save(*args, **kwargs)