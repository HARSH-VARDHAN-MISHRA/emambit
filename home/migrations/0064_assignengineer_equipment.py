# Generated by Django 4.2.7 on 2024-03-18 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0063_alter_userattendance_attendance_date"),
    ]

    operations = [
        migrations.AddField(
            model_name="assignengineer",
            name="equipment",
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
    ]
