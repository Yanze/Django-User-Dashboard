# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-06 19:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userdashboard_app', '0002_auto_20160506_1903'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
