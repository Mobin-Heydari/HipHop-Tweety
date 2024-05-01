# Generated by Django 5.0.4 on 2024-05-01 20:49

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='متن')),
                ('score', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)], verbose_name='امتیاز')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'نظر',
                'verbose_name_plural': 'نظرات',
                'ordering': ['created'],
            },
        ),
        migrations.CreateModel(
            name='CommentReply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reply', models.TextField(verbose_name='پاسخ')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'پاسخ',
                'verbose_name_plural': 'پاسخ ها',
            },
        ),
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True, verbose_name='عنوان')),
                ('slug', models.SlugField(max_length=200, unique=True, verbose_name='اسلاگ')),
                ('artist', models.CharField(max_length=200, verbose_name='آرتیست')),
                ('composer', models.CharField(max_length=200, verbose_name='آهنگساز')),
                ('songwriter', models.CharField(max_length=200, verbose_name='ترانه سرا')),
                ('regulators', models.CharField(max_length=200, verbose_name='تنظیم کننده')),
                ('image', models.ImageField(upload_to='Musices/files/images', verbose_name='تصویر موزیک')),
                ('banner', models.ImageField(upload_to='Musices/files/banner', verbose_name='بنر موزیک')),
                ('music_file', models.FileField(upload_to='Musices/files/mp3', verbose_name='فایل موزیک')),
                ('text', models.TextField(verbose_name='متن')),
                ('release_date', models.DateField(verbose_name='تاریخ اکران')),
                ('likes', models.IntegerField(default=0, verbose_name='لایک ها')),
                ('plays', models.IntegerField(default=0, verbose_name='بلی')),
                ('music_time', models.CharField(max_length=20, verbose_name='زمان موزیک')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'موزیک',
                'verbose_name_plural': 'موزیک ها',
                'ordering': ['release_date'],
            },
        ),
    ]
