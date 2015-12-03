# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('microinsurance', '0007_auto_20151202_1712'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='branchaccess',
            options={'verbose_name_plural': 'Branch Access'},
        ),
        migrations.AlterField(
            model_name='microinsuranceoffered',
            name='Date_Effective_End',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 2, 17, 13, 27, 790153)),
        ),
        migrations.AlterField(
            model_name='microinsuranceoffered',
            name='Date_Effective_Start',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 2, 17, 13, 27, 790094)),
        ),
    ]
