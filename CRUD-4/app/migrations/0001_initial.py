# Generated by Django 5.0.3 on 2024-03-18 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Order",
            fields=[
                ("oid", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=20)),
                ("phone", models.CharField(max_length=10)),
                ("address", models.CharField(max_length=100)),
            ],
            options={
                "db_table": "Order",
            },
        ),
    ]
