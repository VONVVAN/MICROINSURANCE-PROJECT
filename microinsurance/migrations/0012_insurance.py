# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('microinsurance', '0011_insurancetype'),
    ]

    operations = [
        migrations.CreateModel(
            name='Insurance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('Insurance_Name', models.CharField(max_length=225)),
                ('Insurance_Base_Price', models.CharField(default=0, max_length=225)),
                ('Insurance_Price', models.CharField(default=0, max_length=225)),
                ('Age_Limitation', models.IntegerField(default=0)),
                ('Limitation_Per_Person', models.IntegerField(default=0)),
                ('Days_Of_Validity', models.IntegerField(default=0)),
                ('Date_Effective', models.DateTimeField()),
                ('Insurance_Type_Name', models.ForeignKey(to='microinsurance.InsuranceType')),
                ('underwriter_name', models.ForeignKey(to='microinsurance.UnderWriter')),
            ],
        ),
    ]
