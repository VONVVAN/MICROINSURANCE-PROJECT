# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('microinsurance', '0025_auto_20151129_1002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('branch_name', models.CharField(max_length=100, serialize=False, primary_key=True)),
                ('date_created', models.CharField(max_length=25, verbose_name=datetime.datetime.now)),
                ('status', models.CharField(max_length=7, default='Active', choices=[('A', 'Active'), ('I', 'Inactive')])),
            ],
            options={
                'verbose_name_plural': 'Branches',
            },
        ),
        migrations.AlterField(
            model_name='discount',
            name='Discount_Name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='insurance',
            name='Date_Effective_End',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 29, 10, 8, 55, 740266)),
        ),
        migrations.AlterField(
            model_name='insurance',
            name='Date_Effective_Start',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 29, 10, 8, 55, 740171)),
        ),
        migrations.AlterField(
            model_name='insurance',
            name='Insurance_Base_Price',
            field=models.CharField(max_length=100, default=0),
        ),
        migrations.AlterField(
            model_name='insurance',
            name='Insurance_Name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='insurance',
            name='Insurance_Price',
            field=models.CharField(max_length=100, default=0),
        ),
        migrations.AlterField(
            model_name='insurancetype',
            name='Insurance_Type_Name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='underwriter',
            name='underwriter_contact_no',
            field=models.CharField(max_length=11),
        ),
        migrations.AlterField(
            model_name='underwriter',
            name='underwriter_contact_person',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='underwriter',
            name='underwriter_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='usertype',
            name='User_Type_Name',
            field=models.CharField(max_length=100),
        ),
    ]
