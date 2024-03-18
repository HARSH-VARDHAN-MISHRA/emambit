# Generated by Django 4.2.7 on 2024-02-07 06:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0031_remove_visiblepassword_user_delete_projectcompletion_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='project_photos')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectCompletion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_description', models.CharField(blank=True, max_length=500, null=True)),
                ('customer_remark', models.CharField(blank=True, max_length=1000, null=True)),
                ('project_status', models.CharField(default='doing', max_length=150)),
                ('project', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='home.assignengineer')),
                ('project_images', models.ManyToManyField(to='home.projectimage')),
            ],
        ),
    ]
