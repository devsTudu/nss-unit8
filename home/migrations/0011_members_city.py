# Generated by Django 3.2 on 2021-04-20 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_members_image_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='members',
            name='city',
            field=models.CharField(default='null', max_length=100),
            preserve_default=False,
        ),
    ]