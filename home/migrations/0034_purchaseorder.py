# Generated by Django 4.2.7 on 2024-02-09 09:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0033_assignengineer_download_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='PurchaseOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_date', models.CharField(blank=True, max_length=254, null=True)),
                ('order_no', models.CharField(blank=True, max_length=254, null=True)),
                ('quotation_no', models.PositiveIntegerField()),
                ('refrence', models.CharField(blank=True, max_length=254, null=True)),
                ('project_description', models.CharField(blank=True, max_length=24, null=True)),
                ('terms_condition', models.CharField(blank=True, max_length=254, null=True)),
                ('order_description', models.CharField(blank=True, max_length=254, null=True)),
                ('rate', models.PositiveIntegerField()),
                ('quantity', models.PositiveIntegerField()),
                ('subtotal', models.PositiveIntegerField()),
                ('discount', models.PositiveIntegerField()),
                ('gst_percent', models.PositiveIntegerField()),
                ('gst_amount', models.PositiveIntegerField()),
                ('final_amount', models.PositiveIntegerField()),
                ('purchase_company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.addpurchasecomapny')),
            ],
        ),
    ]
