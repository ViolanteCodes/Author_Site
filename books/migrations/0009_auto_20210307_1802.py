# Generated by Django 3.1.7 on 2021-03-07 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0008_auto_20210307_1750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookpage',
            name='release_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
