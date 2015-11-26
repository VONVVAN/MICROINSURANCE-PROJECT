# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('microinsurance', '0003_auto_20151126_0349'),
    ]

    operations = [
        migrations.CreateModel(
            name='SystemUser',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('first_name', models.CharField(max_length=225)),
                ('last_name', models.CharField(max_length=225)),
                ('middle_name', models.CharField(blank=True, max_length=225)),
                ('contact_no', models.CharField(max_length=225)),
                ('branch_name', models.ForeignKey(to='microinsurance.Branch')),
            ],
        ),
        migrations.RemoveField(
            model_name='system_user',
            name='branch_name',
        ),
        migrations.DeleteModel(
            name='System_User',
        ),
    ]
