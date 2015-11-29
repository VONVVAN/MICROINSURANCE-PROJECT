# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('microinsurance', '0027_auto_20151129_1010'),
    ]

    operations = [
        migrations.AddField(
            model_name='discount',
            name='date_created',
            field=models.CharField(max_length=25, default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='insurance',
            name='date_created',
            field=models.CharField(max_length=25, default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='insurancetype',
            name='date_created',
            field=models.CharField(max_length=25, default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='underwriter',
            name='date_created',
            field=models.CharField(max_length=25, default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='useraccess',
            name='date_created',
            field=models.CharField(max_length=25, default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='usertype',
            name='date_created',
            field=models.CharField(max_length=25, default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='insurance',
            name='Date_Effective_End',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 29, 10, 12, 28, 883264)),
        ),
        migrations.AlterField(
            model_name='insurance',
            name='Date_Effective_Start',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 29, 10, 12, 28, 883171)),
        ),
    ]
