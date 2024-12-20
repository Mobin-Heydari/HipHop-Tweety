# Generated by Django 5.0.4 on 2024-05-09 09:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscription', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubscriptionPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='عنوان پلن اشتراک')),
                ('price_pre_month', models.IntegerField(verbose_name='قیمت پلن اشتراک برای هر ماه')),
                ('is_active', models.BooleanField(default=True, verbose_name='وضعیت پلن اشتراک')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'پلن اشتراک',
                'verbose_name_plural': 'پلن های اشتراک',
                'ordering': ['created'],
            },
        ),
        migrations.AddField(
            model_name='usersubscription',
            name='plan',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='plans', to='subscription.subscriptionplan', verbose_name='پلن'),
        ),
    ]
