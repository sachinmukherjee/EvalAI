# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2018-03-16 20:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("challenges", "0032_adds_featured_field_in_challenge")]

    operations = [
        migrations.AlterField(
            model_name="datasetsplit",
            name="codename",
            field=models.CharField(max_length=100),
        )
    ]
