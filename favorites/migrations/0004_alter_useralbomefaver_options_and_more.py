# Generated by Django 5.0.4 on 2024-05-07 04:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('favorites', '0003_alter_usermusicfaver_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='useralbomefaver',
            options={'ordering': ['created'], 'verbose_name': 'علاقمندی آلبوم های کاربر', 'verbose_name_plural': 'علاقمندی آلبوم های کاربران'},
        ),
        migrations.AlterModelOptions(
            name='usermusicfaver',
            options={'ordering': ['created'], 'verbose_name': 'علاقمندی موزیک های کاربر', 'verbose_name_plural': 'علاقمندی موزیک های کاربران'},
        ),
        migrations.RemoveField(
            model_name='useralbomefaver',
            name='is_faver',
        ),
        migrations.RemoveField(
            model_name='useralbomefaver',
            name='updated',
        ),
        migrations.RemoveField(
            model_name='usermusicfaver',
            name='updated',
        ),
    ]