# Generated by Django 3.0.8 on 2020-10-25 05:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('buckets', '0012_auto_20201025_1336'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bucket',
            name='parent_bucket',
        ),
        migrations.AddField(
            model_name='bucket',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='buckets.Bucket'),
        ),
    ]