# Generated by Django 3.1.7 on 2021-03-07 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0009_auto_20210307_1802'),
    ]

    operations = [
        migrations.RenameField(
            model_name='genre',
            old_name='genre_name',
            new_name='genre',
        ),
        migrations.RemoveField(
            model_name='genre',
            name='genre_slug',
        ),
        migrations.AddField(
            model_name='genre',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
