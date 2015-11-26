# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('microinsurance', '0012_insurance'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='insurance',
            name='Date_Effective',
        ),
        migrations.AddField(
            model_name='insurance',
            name='Date_Effective_Start',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 26, 18, 43, 42, 545083)),
        ),
    ]
