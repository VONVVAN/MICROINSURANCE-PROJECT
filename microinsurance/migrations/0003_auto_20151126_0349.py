# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('microinsurance', '0002_auto_20151126_0252'),
    ]

    operations = [
        migrations.CreateModel(
            name='System_User',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('first_name', models.CharField(max_length=225)),
                ('last_name', models.CharField(max_length=225)),
                ('middle_name', models.CharField(blank=True, max_length=225)),
                ('contact_no', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='branch',
            name='id',
        ),
        migrations.AlterField(
            model_name='branch',
            name='branch_name',
            field=models.CharField(serialize=False, primary_key=True, max_length=225),
        ),
        migrations.AddField(
            model_name='system_user',
            name='branch_name',
            field=models.ForeignKey(to='microinsurance.Branch'),
        ),
    ]
