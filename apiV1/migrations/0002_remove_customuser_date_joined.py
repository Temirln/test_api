# Generated by Django 4.2.3 on 2023-07-15 05:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("apiV1", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="customuser",
            name="date_joined",
        ),
    ]
