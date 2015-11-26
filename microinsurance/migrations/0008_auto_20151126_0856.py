# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('microinsurance', '0007_auto_20151126_0506'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='branch',
            options={'verbose_name_plural': 'branches'},
        ),
    ]
