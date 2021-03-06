# Generated by Django 2.2 on 2020-09-29 16:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Assignment_Name', models.CharField(max_length=100)),
                ('Date_Published', models.DateTimeField(auto_now_add=True)),
                ('upload', models.FileField(default='No file uploaded', null=True, upload_to='assignments/')),
                ('Assignment_Content', models.CharField(max_length=10000)),
                ('Course_Title', models.CharField(default='', max_length=255)),
                ('Course_Code', models.CharField(default='', max_length=8)),
                ('Due_Date', models.DateField(default=django.utils.timezone.now)),
                ('Batch', models.CharField(default='', max_length=6)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assignments', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Assignments',
            },
        ),
    ]
