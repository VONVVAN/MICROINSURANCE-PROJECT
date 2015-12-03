# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('microinsurance', '0004_auto_20151201_1248'),
    ]

    operations = [
        migrations.AddField(
            model_name='branch',
            name='branch_manager',
            field=models.CharField(max_length=100, default=''),
        ),
        migrations.AddField(
            model_name='branch',
            name='front_liner',
            field=models.CharField(max_length=100, default=''),
        ),
        migrations.AlterField(
            model_name='microinsuranceoffered',
            name='Date_Effective_End',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 2, 16, 51, 10, 886143)),
        ),
        migrations.AlterField(
            model_name='microinsuranceoffered',
            name='Date_Effective_Start',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 2, 16, 51, 10, 886082)),
        ),
    ]
