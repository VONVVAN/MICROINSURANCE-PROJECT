# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('microinsurance', '0005_auto_20151126_0417'),
    ]

    operations = [
        migrations.CreateModel(
            name='SystemUser',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('first_name', models.CharField(max_length=225)),
                ('last_name', models.CharField(max_length=225)),
                ('middle_name', models.CharField(blank=True, max_length=225)),
                ('contact_no', models.CharField(max_length=225)),
                ('branch_name', models.ForeignKey(to='microinsurance.Branch')),
                ('user_type', models.ForeignKey(to='microinsurance.UserType')),
            ],
        ),
    ]
