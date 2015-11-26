# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('microinsurance', '0010_auto_20151126_0953'),
    ]

    operations = [
        migrations.CreateModel(
            name='InsuranceType',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('Insurance_Type_Name', models.CharField(max_length=225)),
            ],
        ),
    ]
