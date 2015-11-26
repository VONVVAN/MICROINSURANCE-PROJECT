# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('microinsurance', '0004_auto_20151126_0407'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserType',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('user_type', models.CharField(unique=True, max_length=225)),
            ],
        ),
        migrations.RemoveField(
            model_name='systemuser',
            name='branch_name',
        ),
        migrations.DeleteModel(
            name='SystemUser',
        ),
    ]
