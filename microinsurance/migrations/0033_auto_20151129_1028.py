# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('microinsurance', '0032_auto_20151129_1026'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='microinsuranceoffered',
            options={'verbose_name_plural': 'Microinsurance Offered'},
        ),
        migrations.AlterField(
            model_name='microinsuranceoffered',
            name='Date_Effective_End',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 29, 10, 28, 24, 750211)),
        ),
        migrations.AlterField(
            model_name='microinsuranceoffered',
            name='Date_Effective_Start',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 29, 10, 28, 24, 750113)),
        ),
    ]
