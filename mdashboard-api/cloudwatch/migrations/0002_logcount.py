# Generated by Django 5.0.6 on 2024-06-12 08:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cloudwatch', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LogCount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('info_count', models.IntegerField(default=0)),
                ('error_count', models.IntegerField(default=0)),
                ('warn_count', models.IntegerField(default=0)),
                ('log', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='log_count', to='cloudwatch.log')),
            ],
        ),
    ]
