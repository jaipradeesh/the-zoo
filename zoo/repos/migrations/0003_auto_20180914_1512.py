# Generated by Django 2.1.1 on 2018-09-14 15:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("repos", "0002_add_indexes")]

    operations = [
        migrations.AlterModelOptions(
            name="repository", options={"verbose_name_plural": "repositories"}
        )
    ]
