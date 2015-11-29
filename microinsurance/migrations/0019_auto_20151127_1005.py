# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import datetime


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('microinsurance', '0018_auto_20151127_0953'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('url', models.URLField(blank=True, verbose_name='Website')),
                ('company', models.CharField(blank=True, max_length=50)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='insideruser',
            name='user',
        ),
        migrations.AlterField(
            model_name='insurance',
            name='Date_Effective_End',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 27, 10, 5, 56, 636195)),
        ),
        migrations.AlterField(
            model_name='insurance',
            name='Date_Effective_Start',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 27, 10, 5, 56, 636139)),
        ),
        migrations.DeleteModel(
            name='InsiderUser',
        ),
    ]
