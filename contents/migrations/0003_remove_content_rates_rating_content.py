# Generated by Django 4.2.4 on 2023-08-29 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0002_remove_rating_content_content_rates'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='content',
            name='rates',
        ),
        migrations.AddField(
            model_name='rating',
            name='content',
            field=models.ManyToManyField(to='contents.content'),
        ),
    ]
