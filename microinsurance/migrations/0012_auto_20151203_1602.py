# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('microinsurance', '0011_auto_20151203_1246'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='amount_paid',
            field=models.CharField(max_length=5, default='0'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='policyno',
            field=models.CharField(max_length=100, default=''),
        ),
        migrations.AddField(
            model_name='transaction',
            name='quantity',
            field=models.CharField(max_length=3, default='0'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='transcontactno',
            field=models.CharField(max_length=11, default='0'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='transmicro',
            field=models.CharField(max_length=100, default=''),
        ),
        migrations.AlterField(
            model_name='microinsuranceoffered',
            name='Date_Effective_End',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 3, 16, 2, 33, 5611)),
        ),
        migrations.AlterField(
            model_name='microinsuranceoffered',
            name='Date_Effective_Start',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 3, 16, 2, 33, 5553)),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='transfname',
            field=models.CharField(max_length=100, default=''),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='translname',
            field=models.CharField(max_length=100, default=''),
        ),
    ]
