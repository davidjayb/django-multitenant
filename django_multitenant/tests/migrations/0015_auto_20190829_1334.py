# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-08-29 13:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tests", "0014_auto_20190828_1314"),
    ]

    operations = [
        migrations.CreateModel(
            name="MigrationTestReferenceModel",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
            ],
        ),
    ]
