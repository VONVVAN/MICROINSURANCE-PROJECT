# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('microinsurance', '0014_auto_20151126_1843'),
    ]

    operations = [
        migrations.RenameField(
            model_name='insurance',
            old_name='Age_Limitation',
            new_name='Maximum_Age',
        ),
        migrations.AddField(
            model_name='insurance',
            name='Date_Effective_End',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 26, 18, 46, 22, 638620)),
        ),
        migrations.AddField(
            model_name='insurance',
            name='Minimum_Age',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='insurance',
            name='Date_Effective_Start',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 26, 18, 46, 22, 638554)),
        ),
    ]
