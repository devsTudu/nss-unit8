# Generated by Django 3.2 on 2021-04-19 14:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20210419_1254'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='members',
            name='image',
        ),
    ]
