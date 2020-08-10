# Generated by Django 3.0.8 on 2020-08-05 13:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_auto_20200804_0028'),
    ]

    operations = [
        migrations.RenameField(
            model_name='watchlist',
            old_name='stocklist',
            new_name='user',
        ),
        migrations.AddField(
            model_name='watchlist',
            name='symbol',
            field=models.CharField(default=django.utils.timezone.now, max_length=10),
            preserve_default=False,
        ),
    ]