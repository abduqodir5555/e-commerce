# Generated by Django 5.0.4 on 2024-04-29 04:34

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_alter_country_options_alter_media_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ourinstagramstory',
            name='story_link',
            field=models.URLField(validators=[django.core.validators.URLValidator(schemes=['https://www.instagram.com/'])], verbose_name='Story link'),
        ),
    ]