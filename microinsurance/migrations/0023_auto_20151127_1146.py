# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('microinsurance', '0022_auto_20151127_1135'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='useraccess',
            options={'verbose_name_plural': 'UserAccess'},
        ),
        migrations.AlterField(
            model_name='insurance',
            name='Date_Effective_End',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 27, 11, 46, 27, 605943)),
        ),
        migrations.AlterField(
            model_name='insurance',
            name='Date_Effective_Start',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 27, 11, 46, 27, 605885)),
        ),
    ]
