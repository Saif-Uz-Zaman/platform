# Generated by Django 4.2.2 on 2023-08-14 09:56

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("product_management", "0002_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="owner",
        ),
    ]
