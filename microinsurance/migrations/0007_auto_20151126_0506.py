# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('microinsurance', '0006_systemuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='systemuser',
            name='branch_name',
            field=models.ForeignKey(to='microinsurance.Branch', max_length=200),
        ),
        migrations.AlterField(
            model_name='systemuser',
            name='user_type',
            field=models.ForeignKey(to='microinsurance.UserType', max_length=200),
        ),
    ]
