# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('microinsurance', '0002_auto_20151201_1143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='contact_no',
            field=models.CharField(validators=[django.core.validators.RegexValidator('^[^\\d]+$', 'Enter a valid Name. This value may contain only letters', 'invalid')], unique=True, max_length=11),
        ),
        migrations.AlterField(
            model_name='microinsuranceoffered',
            name='Date_Effective_End',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 1, 12, 44, 47, 888039)),
        ),
        migrations.AlterField(
            model_name='microinsuranceoffered',
            name='Date_Effective_Start',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 1, 12, 44, 47, 887982)),
        ),
    ]
