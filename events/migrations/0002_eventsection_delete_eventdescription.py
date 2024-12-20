# Generated by Django 5.0.4 on 2024-05-21 10:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True, verbose_name='عنوان')),
                ('description', models.TextField(blank=True, null=True, verbose_name='توضیحات')),
                ('image', models.ImageField(blank=True, null=True, upload_to='Events/Desciption/images/', verbose_name='تصویر')),
                ('video', models.FileField(blank=True, null=True, upload_to='Events/Desciption/video/', verbose_name='ویدیو')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_description', to='events.event', verbose_name='اتفاق')),
            ],
            options={
                'verbose_name': 'توضیح اتفاق',
                'verbose_name_plural': 'توضیحات اتفاق',
            },
        ),
        migrations.DeleteModel(
            name='EventDescription',
        ),
    ]
