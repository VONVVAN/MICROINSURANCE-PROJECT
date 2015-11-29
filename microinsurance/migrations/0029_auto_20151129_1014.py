# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('microinsurance', '0028_auto_20151129_1012'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Branch',
        ),
        migrations.RemoveField(
            model_name='discount',
            name='Insurance_Name',
        ),
        migrations.RemoveField(
            model_name='insurance',
            name='Insurance_Type_Name',
        ),
        migrations.RemoveField(
            model_name='insurance',
            name='underwriter_name',
        ),
        migrations.RemoveField(
            model_name='useraccess',
            name='User_Type_Name',
        ),
        migrations.RemoveField(
            model_name='useraccess',
            name='user',
        ),
        migrations.DeleteModel(
            name='Discount',
        ),
        migrations.DeleteModel(
            name='Insurance',
        ),
        migrations.DeleteModel(
            name='InsuranceType',
        ),
        migrations.DeleteModel(
            name='UnderWriter',
        ),
        migrations.DeleteModel(
            name='UserAccess',
        ),
        migrations.DeleteModel(
            name='UserType',
        ),
    ]
