# Generated by Django 4.1.2 on 2022-10-26 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0008_cmpachecklist_user_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="cmpachecklist",
            name="billing_type",
            field=models.CharField(blank=True, default="", max_length=50),
        ),
    ]