# Generated by Django 5.0.4 on 2024-05-01 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, max_length=500, null=True, verbose_name='بیوگرافی')),
                ('image', models.ImageField(blank=True, null=True, upload_to='profiles/', verbose_name='تصویر پروفایل')),
                ('full_name', models.CharField(blank=True, max_length=200, null=True, verbose_name='نام کامل کاربر')),
            ],
            options={
                'verbose_name': 'پروفایل کاربر',
                'verbose_name_plural': 'پروفایل کاربران',
            },
        ),
    ]
