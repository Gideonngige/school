# Generated by Django 5.0.6 on 2024-07-29 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apisapp', '0002_messages_remove_vote_choice_remove_poll_created_by_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(default='0710101021', max_length=10)),
                ('password', models.CharField(max_length=10)),
            ],
        ),
    ]
