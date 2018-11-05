# Generated by Django 2.1.2 on 2018-11-01 06:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplyBuffer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_date', models.DateTimeField(auto_now=True, verbose_name='Request Date')),
                ('ent_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='enterprise_id', to=settings.AUTH_USER_MODEL)),
                ('individual_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='individual_id', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
