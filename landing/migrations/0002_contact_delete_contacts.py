# Generated by Django 5.0.4 on 2024-05-09 20:35

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(blank=True, max_length=250, null=True, verbose_name='نام')),
                ('l_name', models.CharField(blank=True, max_length=250, null=True, verbose_name='نام خانوادگی')),
                ('phone', models.CharField(blank=True, max_length=12, null=True, verbose_name='شماره تماس')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, validators=[django.core.validators.EmailValidator], verbose_name='ایمیل')),
                ('message', models.TextField(blank=True, null=True, verbose_name='پیام')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'تماس',
                'verbose_name_plural': 'تماس ها',
            },
        ),
        migrations.DeleteModel(
            name='Contacts',
        ),
    ]