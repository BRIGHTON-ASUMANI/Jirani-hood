# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-23 14:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neighbor', '0002_remove_business_biz'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='business_emails',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='business',
            name='business_name',
            field=models.CharField(max_length=40),
        ),
    ]
