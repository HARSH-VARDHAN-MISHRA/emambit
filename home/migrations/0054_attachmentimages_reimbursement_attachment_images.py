# Generated by Django 4.2.7 on 2024-02-14 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0053_alter_assignengineer_engineer_one'),
    ]

    operations = [
        migrations.CreateModel(
            name='AttachmentImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='attachment_images')),
            ],
        ),
        migrations.AddField(
            model_name='reimbursement',
            name='attachment_images',
            field=models.ManyToManyField(to='home.attachmentimages'),
        ),
    ]
