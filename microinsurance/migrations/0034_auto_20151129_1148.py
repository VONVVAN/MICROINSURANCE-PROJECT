# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('microinsurance', '0033_auto_20151129_1028'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Branch',
        ),
        migrations.AlterField(
            model_name='microinsuranceoffered',
            name='Date_Effective_End',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 29, 11, 48, 32, 552533)),
        ),
        migrations.AlterField(
            model_name='microinsuranceoffered',
            name='Date_Effective_Start',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 29, 11, 48, 32, 552480)),
        ),
        migrations.AlterField(
            model_name='microinsuranceoffered',
            name='date_created',
            field=models.CharField(max_length=26, default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='microinsurancetype',
            name='date_created',
            field=models.CharField(max_length=26, default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='underwriter',
            name='date_created',
            field=models.CharField(max_length=26, default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='useraccess',
            name='date_created',
            field=models.CharField(max_length=26, default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='usertype',
            name='date_created',
            field=models.CharField(max_length=26, default=datetime.datetime.now),
        ),
    ]
