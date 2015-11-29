# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('microinsurance', '0030_auto_20151129_1014'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='discount',
            name='Insurance_Name',
        ),
        migrations.AlterField(
            model_name='insurance',
            name='Date_Effective_End',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 29, 10, 15, 53, 317092)),
        ),
        migrations.AlterField(
            model_name='insurance',
            name='Date_Effective_Start',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 29, 10, 15, 53, 316993)),
        ),
        migrations.DeleteModel(
            name='Discount',
        ),
    ]
