# Generated by Django 3.2.4 on 2021-06-22 10:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainSite', '0007_alter_user_salt'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='salt',
        ),
    ]
