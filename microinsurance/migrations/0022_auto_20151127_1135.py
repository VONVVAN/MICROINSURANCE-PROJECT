# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import datetime


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('microinsurance', '0021_auto_20151127_1051'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAccess',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('status', models.CharField(choices=[('A', 'Active'), ('I', 'Inactive')], max_length=7)),
                ('User_Type_Name', models.ForeignKey(to='microinsurance.UserType')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.AddField(
            model_name='branch',
            name='status',
            field=models.CharField(choices=[('A', 'Active'), ('I', 'Inactive')], default='Active', max_length=7),
        ),
        migrations.AddField(
            model_name='discount',
            name='status',
            field=models.CharField(choices=[('A', 'Active'), ('I', 'Inactive')], default='Active', max_length=7),
        ),
        migrations.AddField(
            model_name='insurance',
            name='status',
            field=models.CharField(choices=[('A', 'Active'), ('I', 'Inactive')], default='Active', max_length=7),
        ),
        migrations.AddField(
            model_name='insurancetype',
            name='status',
            field=models.CharField(choices=[('A', 'Active'), ('I', 'Inactive')], default='Active', max_length=7),
        ),
        migrations.AddField(
            model_name='underwriter',
            name='status',
            field=models.CharField(choices=[('A', 'Active'), ('I', 'Inactive')], default='Active', max_length=7),
        ),
        migrations.AlterField(
            model_name='insurance',
            name='Date_Effective_End',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 27, 11, 35, 46, 726200)),
        ),
        migrations.AlterField(
            model_name='insurance',
            name='Date_Effective_Start',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 27, 11, 35, 46, 726140)),
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
