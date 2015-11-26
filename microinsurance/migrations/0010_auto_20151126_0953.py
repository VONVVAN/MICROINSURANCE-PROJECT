# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('microinsurance', '0009_auto_20151126_0952'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UnderWriters',
            new_name='UnderWriter',
        ),
    ]
