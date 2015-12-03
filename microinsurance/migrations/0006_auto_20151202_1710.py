# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import datetime


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('microinsurance', '0005_auto_20151202_1651'),
    ]

    operations = [
        migrations.CreateModel(
            name='BranchAccess',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('date_created', models.CharField(default=datetime.datetime.now, max_length=26)),
                ('status', models.CharField(choices=[('A', 'Active'), ('I', 'Inactive')], max_length=7)),
                ('User_Type_Name', models.ForeignKey(to='microinsurance.UserType')),
            ],
            options={
                'verbose_name_plural': 'User Access',
            },
        ),
        migrations.RemoveField(
            model_name='useraccess',
            name='User_Type_Name',
        ),
        migrations.RemoveField(
            model_name='useraccess',
            name='user',
        ),
        migrations.RemoveField(
            model_name='branch',
            name='branch_manager',
        ),
        migrations.RemoveField(
            model_name='branch',
            name='front_liner',
        ),
        migrations.AlterField(
            model_name='microinsuranceoffered',
            name='Date_Effective_End',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 2, 17, 10, 47, 540792)),
        ),
        migrations.AlterField(
            model_name='microinsuranceoffered',
            name='Date_Effective_Start',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 2, 17, 10, 47, 540731)),
        ),
        migrations.DeleteModel(
            name='UserAccess',
        ),
        migrations.AddField(
            model_name='branchaccess',
            name='branch_name',
            field=models.ForeignKey(to='microinsurance.Branch'),
        ),
        migrations.AddField(
            model_name='branchaccess',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
    ]
