# Generated by Django 5.0.3 on 2024-03-19 05:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0003_alter_task_time"),
    ]

    operations = [
        migrations.AlterModelTable(
            name="task",
            table="task",
        ),
    ]