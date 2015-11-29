# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import datetime


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('microinsurance', '0017_auto_20151127_0939'),
    ]

    operations = [
        migrations.CreateModel(
            name='InsiderUser',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('company_name', models.CharField(max_length=225, blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='discount',
            name='Insurance_Name',
        ),
        migrations.AddField(
            model_name='discount',
            name='Insurance_Name',
            field=models.ManyToManyField(to='microinsurance.Insurance'),
        ),
        migrations.AlterField(
            model_name='insurance',
            name='Date_Effective_End',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 27, 9, 53, 9, 503447)),
        ),
        migrations.AlterField(
            model_name='insurance',
            name='Date_Effective_Start',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 27, 9, 53, 9, 503387)),
        ),
    ]
