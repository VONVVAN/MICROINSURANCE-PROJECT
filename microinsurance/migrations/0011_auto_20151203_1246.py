# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('microinsurance', '0010_auto_20151203_1133'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('transfname', models.CharField(max_length=100)),
                ('translname', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='applicant',
            name='contact_no',
            field=models.CharField(max_length=11, validators=[django.core.validators.RegexValidator('^[0-9]+$', 'Enter a valid Name. This value may contain only letters', 'invalid')]),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='middle_name',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='suffix',
            field=models.CharField(max_length=5, blank=True),
        ),
        migrations.AlterField(
            model_name='microinsuranceoffered',
            name='Date_Effective_End',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 3, 12, 46, 28, 93282)),
        ),
        migrations.AlterField(
            model_name='microinsuranceoffered',
            name='Date_Effective_Start',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 3, 12, 46, 28, 93225)),
        ),
    ]
