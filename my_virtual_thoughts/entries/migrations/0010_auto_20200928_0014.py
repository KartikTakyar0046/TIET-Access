# Generated by Django 2.2 on 2020-09-27 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0009_auto_20200927_2341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='Batch',
            field=models.CharField(blank=True, choices=[('24', 'COE-24'), ('25', 'COE-25'), ('26', 'COE-26'), ('27', 'COE-27'), ('28', 'COE-28')], max_length=12, null=True),
        ),
    ]