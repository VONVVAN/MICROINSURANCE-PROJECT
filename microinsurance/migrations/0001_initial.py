# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import datetime
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Applicant',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('middle_name', models.CharField(max_length=100)),
                ('suffix', models.CharField(max_length=5)),
                ('birthdate', models.CharField(max_length=100)),
                ('contact_no', models.CharField(unique=True, max_length=11)),
                ('address', models.CharField(max_length=100)),
                ('microinsurance', models.CharField(max_length=100)),
                ('quantity', models.CharField(max_length=3)),
                ('policy_no', models.CharField(unique=True, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('branch_name', models.CharField(unique=True, max_length=100, validators=[django.core.validators.RegexValidator('^[\\s\\w.-]+$', 'Enter a valid Branch Name. This value may contain only letters, numbers and /./-/_ characters.', 'invalid')])),
                ('date_created', models.CharField(max_length=26, default=datetime.datetime.now)),
                ('status', models.CharField(choices=[('A', 'Active'), ('I', 'Inactive')], max_length=7, default='Active')),
            ],
            options={
                'verbose_name_plural': 'Branches',
            },
        ),
        migrations.CreateModel(
            name='MicroinsuranceOffered',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('Microinsurance_Code', models.CharField(unique=True, max_length=10, validators=[django.core.validators.RegexValidator('^[\\d\\w-]+$', 'Enter a valid Code. This value may contain numbers, letters and "-" character', 'invalid')])),
                ('Microinsurance_Name', models.CharField(unique=True, default='', max_length=100, validators=[django.core.validators.RegexValidator('^[^\\d]+$', 'Enter a valid Name. This value may contain only letters', 'invalid')])),
                ('Microinsurance_Description', models.TextField(max_length=200, validators=[django.core.validators.RegexValidator('^[\\s\\d\\w-]+$', 'Enter a valid Name. This value may contain only letters, numbers and ".-" characters', 'invalid')])),
                ('Microinsurance_Base_Price', models.CharField(max_length=100, default=0)),
                ('Microinsurance_Price', models.CharField(max_length=100, default=0)),
                ('Minimum_Age', models.CharField(default=0, max_length=3, validators=[django.core.validators.RegexValidator('^[0-9]+$', 'Enter a valid Age. This value may contain only numbers', 'invalid')])),
                ('Maximum_Age', models.CharField(default=0, max_length=3, validators=[django.core.validators.RegexValidator('^[0-9]+$', 'Enter a valid Age. This value may contain only numbers', 'invalid')])),
                ('Limitation_Per_Person', models.CharField(default=0, max_length=2, validators=[django.core.validators.RegexValidator('^[0-9]+$', 'Enter a valid Numebr. This value may contain only numbers', 'invalid')])),
                ('Days_Of_Validity', models.CharField(default=0, max_length=3, validators=[django.core.validators.RegexValidator('^[0-9]+$', 'Enter a valid Number. This value may contain only numbers', 'invalid')])),
                ('Date_Effective_Start', models.DateTimeField(default=datetime.datetime(2015, 12, 1, 11, 43, 14, 507728))),
                ('Date_Effective_End', models.DateTimeField(default=datetime.datetime(2015, 12, 1, 11, 43, 14, 507788))),
                ('date_created', models.CharField(max_length=26, default=datetime.datetime.now)),
                ('status', models.CharField(choices=[('A', 'Active'), ('I', 'Inactive')], max_length=7, default='Active')),
            ],
            options={
                'verbose_name_plural': 'Microinsurance Offered',
            },
        ),
        migrations.CreateModel(
            name='MicroinsuranceType',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('Microinsurance_Type_Name', models.CharField(unique=True, max_length=100, validators=[django.core.validators.RegexValidator('^[^\\d]+$', 'Enter a valid Name. This value may contain only letters', 'invalid')])),
                ('date_created', models.CharField(max_length=26, default=datetime.datetime.now)),
                ('status', models.CharField(choices=[('A', 'Active'), ('I', 'Inactive')], max_length=7, default='Active')),
            ],
        ),
        migrations.CreateModel(
            name='UnderWriter',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('underwriter_name', models.CharField(unique=True, max_length=100, validators=[django.core.validators.RegexValidator('^[^\\d]+$', 'Enter a valid UnderWriter Name. This value may contain only letters, numbers and ./-/_ characters.', 'invalid')])),
                ('underwriter_address', models.TextField(max_length=100, validators=[django.core.validators.RegexValidator('^[\\s\\w.-]+$', 'Enter a valid Address. This value may contain only letters, numbers and ./-/_ characters.', 'invalid')])),
                ('underwriter_contact_person', models.CharField(max_length=100, validators=[django.core.validators.RegexValidator('^[^\\d]+$', 'Enter a valid Name. This value may contain only letters', 'invalid')])),
                ('underwriter_contact_no', models.CharField(unique=True, max_length=11, validators=[django.core.validators.RegexValidator('^[0-9]+$', 'Enter a valid contact no. only accepts numbers', 'invalid')])),
                ('date_created', models.CharField(max_length=26, default=datetime.datetime.now)),
                ('status', models.CharField(choices=[('A', 'Active'), ('I', 'Inactive')], max_length=7, default='Active')),
            ],
        ),
        migrations.CreateModel(
            name='UserAccess',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('date_created', models.CharField(max_length=26, default=datetime.datetime.now)),
                ('status', models.CharField(choices=[('A', 'Active'), ('I', 'Inactive')], max_length=7)),
            ],
            options={
                'verbose_name_plural': 'User Access',
            },
        ),
        migrations.CreateModel(
            name='UserType',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('User_Type_Name', models.CharField(unique=True, max_length=100, validators=[django.core.validators.RegexValidator('^[^\\d]+$', 'Enter a valid Name. This value may contain only letters', 'invalid')])),
                ('date_created', models.CharField(max_length=26, default=datetime.datetime.now)),
                ('status', models.CharField(choices=[('A', 'Active'), ('I', 'Inactive')], max_length=7, default='Active')),
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
