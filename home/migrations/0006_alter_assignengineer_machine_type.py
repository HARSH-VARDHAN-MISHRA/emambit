# Generated by Django 4.2.7 on 2024-02-01 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_assignengineer_company_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignengineer',
            name='machine_type',
            field=models.CharField(max_length=254),
        ),
    ]
