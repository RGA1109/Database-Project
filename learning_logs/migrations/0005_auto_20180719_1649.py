# Generated by Django 2.0.5 on 2018-07-19 16:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0004_auto_20180719_1455'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='expiration_date',
            field=models.DateField(default=django.utils.timezone.now),
        )
    ]
