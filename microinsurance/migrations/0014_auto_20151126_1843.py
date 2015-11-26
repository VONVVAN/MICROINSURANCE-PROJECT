# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('microinsurance', '0013_auto_20151126_1843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='insurance',
            name='Date_Effective_Start',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 26, 18, 43, 45, 180982)),
        ),
    ]
