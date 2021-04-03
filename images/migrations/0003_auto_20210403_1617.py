# Generated by Django 3.1.7 on 2021-04-03 16:17

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0002_image_result_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='random_from',
            field=models.SmallIntegerField(default=0, help_text='Value from -255 to 255', validators=[django.core.validators.MinValueValidator(-255), django.core.validators.MaxValueValidator(255)]),
        ),
        migrations.AddField(
            model_name='image',
            name='random_to',
            field=models.SmallIntegerField(default=0, help_text='Value from -255 to 255', validators=[django.core.validators.MinValueValidator(-255), django.core.validators.MaxValueValidator(255)]),
        ),
    ]