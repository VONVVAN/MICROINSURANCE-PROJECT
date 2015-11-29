# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('microinsurance', '0020_auto_20151127_1006'),
    ]

    operations = [
        migrations.AddField(
            model_name='usertype',
            name='status',
            field=models.CharField(choices=[('A', 'Active'), ('I', 'Inactive')], max_length=7, default='Active'),
        ),
        migrations.AlterField(
            model_name='insurance',
            name='Date_Effective_End',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 27, 10, 51, 1, 220008)),
        ),
        migrations.AlterField(
            model_name='insurance',
            name='Date_Effective_Start',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 27, 10, 51, 1, 219951)),
        ),
    ]
