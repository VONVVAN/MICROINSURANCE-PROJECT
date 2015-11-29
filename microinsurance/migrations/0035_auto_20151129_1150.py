# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('microinsurance', '0034_auto_20151129_1148'),
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('branch_name', models.CharField(max_length=100, unique=True)),
                ('date_created', models.CharField(default=datetime.datetime.now, max_length=26)),
                ('status', models.CharField(default='Active', max_length=7, choices=[('A', 'Active'), ('I', 'Inactive')])),
            ],
            options={
                'verbose_name_plural': 'Branches',
            },
        ),
        migrations.AlterField(
            model_name='microinsuranceoffered',
            name='Date_Effective_End',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 29, 11, 50, 43, 33204)),
        ),
        migrations.AlterField(
            model_name='microinsuranceoffered',
            name='Date_Effective_Start',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 29, 11, 50, 43, 33148)),
        ),
        migrations.AlterField(
            model_name='microinsuranceoffered',
            name='Microinsurance_Code',
            field=models.CharField(max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='microinsuranceoffered',
            name='Microinsurance_Name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='microinsurancetype',
            name='Microinsurance_Type_Name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='underwriter',
            name='underwriter_contact_no',
            field=models.CharField(max_length=11, unique=True),
        ),
        migrations.AlterField(
            model_name='underwriter',
            name='underwriter_name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='usertype',
            name='User_Type_Name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
