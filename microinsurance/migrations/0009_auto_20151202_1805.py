# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('microinsurance', '0008_auto_20151202_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='contact_no',
            field=models.CharField(max_length=11, validators=[django.core.validators.RegexValidator('^[^\\d]+$', 'Enter a valid Name. This value may contain only letters', 'invalid')]),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='policy_no',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='microinsuranceoffered',
            name='Date_Effective_End',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 2, 18, 5, 1, 654873)),
        ),
        migrations.AlterField(
            model_name='microinsuranceoffered',
            name='Date_Effective_Start',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 2, 18, 5, 1, 654813)),
        ),
    ]
