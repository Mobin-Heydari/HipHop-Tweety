# Generated by Django 5.0.4 on 2024-05-09 10:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('favorites', '0005_remove_userfavorite_user_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='useralbumfavorite',
            options={'ordering': ['created'], 'verbose_name': 'آلبوم', 'verbose_name_plural': 'آلبوم ها'},
        ),
        migrations.AlterModelOptions(
            name='usermusicfavorite',
            options={'ordering': ['created'], 'verbose_name': 'موزیک', 'verbose_name_plural': 'موزیک ها'},
        ),
    ]
