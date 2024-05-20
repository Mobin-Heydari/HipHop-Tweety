# Generated by Django 5.0.4 on 2024-05-09 20:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=250, verbose_name='نام')),
                ('l_name', models.CharField(max_length=250, verbose_name='نام خانوادگی')),
                ('phone', models.CharField(max_length=12, verbose_name='شماره تماس')),
                ('email', models.EmailField(max_length=254, validators=[django.core.validators.EmailValidator], verbose_name='ایمیل')),
                ('message', models.TextField(verbose_name='پیام')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'تماس',
                'verbose_name_plural': 'تماس ها',
            },
        ),
    ]
