# Generated by Django 3.1.7 on 2021-03-09 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0018_bookpage_teaser'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookpage',
            name='repeat_in_subnav',
            field=models.BooleanField(default=False, help_text="If checked, a link to this page will be repeated alongside it's direct children when displaying a sub-navigation for this page.", verbose_name='repeat in sub-navigation'),
        ),
        migrations.AddField(
            model_name='bookpage',
            name='repeated_item_text',
            field=models.CharField(blank=True, help_text="e.g. 'Section home' or 'Overview'. If left blank, the page title will be used.", max_length=255, verbose_name='repeated item link text'),
        ),
    ]
