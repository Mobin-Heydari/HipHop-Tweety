# Generated by Django 5.0.4 on 2024-05-02 10:34

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alboms', '0002_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='عنوان')),
                ('text', models.TextField(verbose_name='متن')),
                ('score', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)], verbose_name='امتیاز')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('albome', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='albome_comments', to='alboms.albom', verbose_name='آلبوم')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_albome_comments', to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
            options={
                'verbose_name': 'نظر آلبوم',
                'verbose_name_plural': 'نظرات آلبوم',
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
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='albome_comment_replies', to='alboms.comment', verbose_name='نظر')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_albome_replies', to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
            options={
                'verbose_name': 'پاسخ',
                'verbose_name_plural': 'پاسخ ها',
            },
        ),
        migrations.DeleteModel(
            name='AlbomComment',
        ),
    ]
