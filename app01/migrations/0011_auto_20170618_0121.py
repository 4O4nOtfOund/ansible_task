# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-18 01:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0010_auto_20170618_0109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='comment',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='\u5907\u6ce8'),
        ),
        migrations.AlterField(
            model_name='group',
            name='name',
            field=models.CharField(max_length=50, unique=True, verbose_name='\u7ec4\u540d'),
        ),
        migrations.AlterField(
            model_name='host',
            name='group',
            field=models.CharField(max_length=50, verbose_name='\u7ec4\u522b'),
        ),
        migrations.AlterField(
            model_name='host',
            name='name',
            field=models.GenericIPAddressField(verbose_name='\u4e3b\u673a\u5730\u5740'),
        ),
        migrations.AlterField(
            model_name='task',
            name='host',
            field=models.TextField(verbose_name='\u4efb\u52a1\u4e3b\u673a'),
        ),
        migrations.AlterField(
            model_name='task',
            name='name',
            field=models.CharField(max_length=50, verbose_name='\u4efb\u52a1\u63cf\u8ff0'),
        ),
    ]
