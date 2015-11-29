# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('microinsurance', '0029_auto_20151129_1014'),
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('branch_name', models.CharField(max_length=100, serialize=False, primary_key=True)),
                ('date_created', models.CharField(default=datetime.datetime.now, max_length=25)),
                ('status', models.CharField(choices=[('A', 'Active'), ('I', 'Inactive')], default='Active', max_length=7)),
            ],
            options={
                'verbose_name_plural': 'Branches',
            },
        ),
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('Discount_Name', models.CharField(max_length=100)),
                ('Percentage', models.IntegerField()),
                ('Date_Start', models.DateTimeField(default=datetime.datetime.now)),
                ('Date_End', models.DateTimeField(default=datetime.datetime.now)),
                ('date_created', models.CharField(default=datetime.datetime.now, max_length=25)),
                ('status', models.CharField(choices=[('A', 'Active'), ('I', 'Inactive')], default='Active', max_length=7)),
            ],
        ),
        migrations.CreateModel(
            name='Insurance',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('Insurance_Name', models.CharField(max_length=100)),
                ('Insurance_Base_Price', models.CharField(default=0, max_length=100)),
                ('Insurance_Price', models.CharField(default=0, max_length=100)),
                ('Minimum_Age', models.IntegerField(default=0)),
                ('Maximum_Age', models.IntegerField(default=0)),
                ('Limitation_Per_Person', models.IntegerField(default=0)),
                ('Days_Of_Validity', models.IntegerField(default=0)),
                ('Date_Effective_Start', models.DateTimeField(default=datetime.datetime(2015, 11, 29, 10, 14, 34, 547856))),
                ('Date_Effective_End', models.DateTimeField(default=datetime.datetime(2015, 11, 29, 10, 14, 34, 547959))),
                ('date_created', models.CharField(default=datetime.datetime.now, max_length=25)),
                ('status', models.CharField(choices=[('A', 'Active'), ('I', 'Inactive')], default='Active', max_length=7)),
            ],
        ),
        migrations.CreateModel(
            name='InsuranceType',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('Insurance_Type_Name', models.CharField(max_length=100)),
                ('date_created', models.CharField(default=datetime.datetime.now, max_length=25)),
                ('status', models.CharField(choices=[('A', 'Active'), ('I', 'Inactive')], default='Active', max_length=7)),
            ],
        ),
        migrations.CreateModel(
            name='UnderWriter',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('underwriter_name', models.CharField(max_length=100)),
                ('underwriter_address', models.TextField()),
                ('underwriter_contact_person', models.CharField(max_length=100)),
                ('underwriter_contact_no', models.CharField(max_length=11)),
                ('date_created', models.CharField(default=datetime.datetime.now, max_length=25)),
                ('status', models.CharField(choices=[('A', 'Active'), ('I', 'Inactive')], default='Active', max_length=7)),
            ],
        ),
        migrations.CreateModel(
            name='UserAccess',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('date_created', models.CharField(default=datetime.datetime.now, max_length=25)),
                ('status', models.CharField(choices=[('A', 'Active'), ('I', 'Inactive')], max_length=7)),
            ],
            options={
                'verbose_name_plural': 'User Access',
            },
        ),
        migrations.CreateModel(
            name='UserType',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('User_Type_Name', models.CharField(max_length=100)),
                ('date_created', models.CharField(default=datetime.datetime.now, max_length=25)),
                ('status', models.CharField(choices=[('A', 'Active'), ('I', 'Inactive')], default='Active', max_length=7)),
            ],
        ),
        migrations.AddField(
            model_name='useraccess',
            name='User_Type_Name',
            field=models.ForeignKey(to='microinsurance.UserType'),
        ),
        migrations.AddField(
            model_name='useraccess',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='insurance',
            name='Insurance_Type_Name',
            field=models.ForeignKey(to='microinsurance.InsuranceType'),
        ),
        migrations.AddField(
            model_name='insurance',
            name='underwriter_name',
            field=models.ForeignKey(to='microinsurance.UnderWriter'),
        ),
        migrations.AddField(
            model_name='discount',
            name='Insurance_Name',
            field=models.ManyToManyField(to='microinsurance.Insurance'),
        ),
    ]
