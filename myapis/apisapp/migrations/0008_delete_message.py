# Generated by Django 5.0.6 on 2024-08-03 18:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apisapp', '0007_message_remove_messages_time_messages_email_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Message',
        ),
    ]
