# Generated by Django 4.2.7 on 2024-02-02 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_assignengineer_ending_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignengineer',
            name='ending_date',
            field=models.CharField(blank=True, default='Work on Progress', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='assignengineer',
            name='work_status',
            field=models.CharField(blank=True, default='Doing', max_length=100, null=True),
        ),
    ]
