# Generated by Django 3.0.8 on 2020-10-26 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buckets', '0002_auto_20201026_1304'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Icon',
        ),
        migrations.AddField(
            model_name='bucket',
            name='icon',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
