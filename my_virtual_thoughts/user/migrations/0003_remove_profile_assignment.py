# Generated by Django 2.2 on 2020-09-29 19:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_profile_assignment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='assignment',
        ),
    ]