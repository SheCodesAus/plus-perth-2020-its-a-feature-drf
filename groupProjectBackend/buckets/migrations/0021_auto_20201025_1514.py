# Generated by Django 3.0.8 on 2020-10-25 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buckets', '0020_auto_20201025_1410'),
    ]

    operations = [
        migrations.AddField(
            model_name='bucket',
            name='owner',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transaction',
            name='owner',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
