# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-08 13:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Repository",
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
                ("gitlab_id", models.IntegerField(unique=True)),
                ("owner", models.CharField(max_length=100)),
                ("name", models.CharField(max_length=100)),
                ("url", models.URLField(max_length=500)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name="repository", unique_together=set([("owner", "name")])
        ),
    ]
