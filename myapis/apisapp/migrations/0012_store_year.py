# Generated by Django 5.0.6 on 2024-08-13 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apisapp', '0011_store'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='year',
            field=models.IntegerField(default=2024),
        ),
    ]
