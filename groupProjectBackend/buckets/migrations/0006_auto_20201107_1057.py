# Generated by Django 3.0.8 on 2020-11-07 02:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('buckets', '0005_auto_20201107_1014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='category_bucket',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='expenses', to='buckets.Bucket'),
        ),
    ]
