# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-02-22 19:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('handy_helper_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='author_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
