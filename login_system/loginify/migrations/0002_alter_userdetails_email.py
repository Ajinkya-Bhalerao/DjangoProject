# Generated by Django 5.1 on 2024-08-12 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("loginify", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userdetails",
            name="email",
            field=models.EmailField(max_length=50, unique=True),
        ),
    ]
