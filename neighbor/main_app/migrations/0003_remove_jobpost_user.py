# Generated by Django 3.1.4 on 2020-12-16 03:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_auto_20201215_1856'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobpost',
            name='user',
        ),
    ]