# Generated by Django 3.2 on 2021-04-25 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20210423_1757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='photo',
            field=models.ImageField(null=True, upload_to='photos'),
        ),
    ]
