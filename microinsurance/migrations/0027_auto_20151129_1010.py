# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('microinsurance', '0026_auto_20151129_1008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branch',
            name='date_created',
            field=models.CharField(default=datetime.datetime.now, max_length=25),
        ),
        migrations.AlterField(
            model_name='insurance',
            name='Date_Effective_End',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 29, 10, 10, 33, 498003)),
        ),
        migrations.AlterField(
            model_name='insurance',
            name='Date_Effective_Start',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 29, 10, 10, 33, 497912)),
        ),
    ]
