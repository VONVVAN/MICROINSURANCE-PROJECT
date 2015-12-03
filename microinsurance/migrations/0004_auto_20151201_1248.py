# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('microinsurance', '0003_auto_20151201_1244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='microinsuranceoffered',
            name='Date_Effective_End',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 1, 12, 48, 34, 419049)),
        ),
        migrations.AlterField(
            model_name='microinsuranceoffered',
            name='Date_Effective_Start',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 1, 12, 48, 34, 418990)),
        ),
    ]
