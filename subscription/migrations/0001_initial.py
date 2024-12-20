# Generated by Django 5.0.4 on 2024-05-09 08:37

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserSubscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField(verbose_name='تاریخ شروع اشتراک')),
                ('end_date', models.DateTimeField(verbose_name='تاریخ اتمام اشتراک')),
                ('is_active', models.BooleanField(default=False, verbose_name='وضعیت اشتراک')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_sub', to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
            options={
                'verbose_name': 'اشتراک کاربر',
                'verbose_name_plural': 'اشتراک کاربران',
            },
        ),
    ]
