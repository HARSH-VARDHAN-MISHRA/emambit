# Generated by Django 4.2.7 on 2024-02-09 10:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0035_purchaseorder_serial_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchaseorder',
            name='serial_number',
        ),
    ]
