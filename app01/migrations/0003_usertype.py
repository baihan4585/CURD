# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-14 15:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_role'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('xxx', models.CharField(max_length=32)),
            ],
        ),
    ]
