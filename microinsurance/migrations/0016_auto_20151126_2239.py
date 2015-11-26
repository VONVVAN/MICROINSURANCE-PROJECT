# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('microinsurance', '0015_auto_20151126_1846'),
    ]

    operations = [
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('Discount_Name', models.CharField(max_length=225)),
                ('Percentage', models.IntegerField()),
                ('Date_Start', models.DateTimeField(default=datetime.datetime.now)),
                ('Date_End', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.AlterField(
            model_name='insurance',
            name='Date_Effective_End',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 26, 22, 39, 43, 407294)),
        ),
        migrations.AlterField(
            model_name='insurance',
            name='Date_Effective_Start',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 26, 22, 39, 43, 407238)),
        ),
        migrations.AddField(
            model_name='discount',
            name='Insurance_Name',
            field=models.ForeignKey(to='microinsurance.Insurance'),
        ),
    ]
