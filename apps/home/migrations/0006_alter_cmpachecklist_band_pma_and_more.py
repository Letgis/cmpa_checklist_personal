# Generated by Django 4.1.2 on 2022-10-18 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0005_auto_20221014_2032"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cmpachecklist",
            name="band_pma",
            field=models.CharField(blank=True, default="", max_length=6),
        ),
        migrations.AlterField(
            model_name="cmpachecklist",
            name="band_pmo",
            field=models.CharField(blank=True, default="", max_length=6),
        ),
    ]
