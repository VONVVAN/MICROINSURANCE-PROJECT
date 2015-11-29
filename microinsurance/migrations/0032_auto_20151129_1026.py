# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('microinsurance', '0031_auto_20151129_1015'),
    ]

    operations = [
        migrations.CreateModel(
            name='MicroinsuranceOffered',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('Microinsurance_Code', models.CharField(max_length=10)),
                ('Microinsurance_Name', models.CharField(max_length=100)),
                ('Microinsurance_Description', models.TextField(max_length=200)),
                ('Microinsurance_Base_Price', models.CharField(max_length=100, default=0)),
                ('Microinsurance_Price', models.CharField(max_length=100, default=0)),
                ('Minimum_Age', models.IntegerField(default=0)),
                ('Maximum_Age', models.IntegerField(default=0)),
                ('Limitation_Per_Person', models.IntegerField(default=0)),
                ('Days_Of_Validity', models.IntegerField(default=0)),
                ('Date_Effective_Start', models.DateTimeField(default=datetime.datetime(2015, 11, 29, 10, 26, 27, 146439))),
                ('Date_Effective_End', models.DateTimeField(default=datetime.datetime(2015, 11, 29, 10, 26, 27, 146532))),
                ('date_created', models.CharField(max_length=25, default=datetime.datetime.now)),
                ('status', models.CharField(max_length=7, choices=[('A', 'Active'), ('I', 'Inactive')], default='Active')),
            ],
        ),
        migrations.RenameModel(
            old_name='InsuranceType',
            new_name='MicroinsuranceType',
        ),
        migrations.RemoveField(
            model_name='insurance',
            name='Insurance_Type_Name',
        ),
        migrations.RemoveField(
            model_name='insurance',
            name='underwriter_name',
        ),
        migrations.RenameField(
            model_name='microinsurancetype',
            old_name='Insurance_Type_Name',
            new_name='Microinsurance_Type_Name',
        ),
        migrations.DeleteModel(
            name='Insurance',
        ),
        migrations.AddField(
            model_name='microinsuranceoffered',
            name='Microinsurance_Type_Name',
            field=models.ForeignKey(to='microinsurance.MicroinsuranceType'),
        ),
        migrations.AddField(
            model_name='microinsuranceoffered',
            name='underwriter_name',
            field=models.ForeignKey(to='microinsurance.UnderWriter'),
        ),
    ]
