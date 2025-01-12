# Generated by Django 5.0.6 on 2024-07-31 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apisapp', '0004_rename_phone_user_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='admission_no',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='billed',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='classteacher',
            field=models.CharField(default='none', max_length=50),
        ),
        migrations.AddField(
            model_name='user',
            name='form',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='paid',
            field=models.IntegerField(default=0),
        ),
    ]
