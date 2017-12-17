# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-17 14:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0004_auto_20171217_2208'),
    ]

    operations = [
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostname', models.CharField(max_length=32, verbose_name='主机名')),
                ('ip', models.GenericIPAddressField(protocol='ipv4', verbose_name='IP')),
                ('port', models.IntegerField(verbose_name='端口')),
            ],
        ),
    ]