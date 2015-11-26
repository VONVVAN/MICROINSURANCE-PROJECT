# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('microinsurance', '0008_auto_20151126_0856'),
    ]

    operations = [
        migrations.CreateModel(
            name='UnderWriters',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('underwriter_name', models.CharField(max_length=225)),
                ('underwriter_address', models.TextField()),
                ('underwriter_contact_person', models.CharField(max_length=225)),
                ('underwriter_contact_no', models.CharField(max_length=225)),
            ],
        ),
        migrations.RemoveField(
            model_name='systemuser',
            name='branch_name',
        ),
        migrations.RemoveField(
            model_name='systemuser',
            name='user_type',
        ),
        migrations.DeleteModel(
            name='SystemUser',
        ),
        migrations.DeleteModel(
            name='UserType',
        ),
    ]
