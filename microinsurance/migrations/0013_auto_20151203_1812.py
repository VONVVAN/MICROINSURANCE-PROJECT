# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('microinsurance', '0012_auto_20151203_1602'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='transdate',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='microinsuranceoffered',
            name='Date_Effective_End',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 3, 18, 12, 44, 907803)),
        ),
        migrations.AlterField(
            model_name='microinsuranceoffered',
            name='Date_Effective_Start',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 3, 18, 12, 44, 907744)),
        ),
    ]
