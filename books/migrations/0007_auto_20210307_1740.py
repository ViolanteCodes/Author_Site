# Generated by Django 3.1.7 on 2021-03-07 17:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_auto_20210307_1734'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contentwarning',
            old_name='warning',
            new_name='warning_name',
        ),
        migrations.RenameField(
            model_name='genre',
            old_name='name',
            new_name='genre_name',
        ),
    ]
