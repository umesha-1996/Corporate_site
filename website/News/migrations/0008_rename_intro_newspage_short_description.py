# Generated by Django 5.1 on 2025-05-22 12:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0007_newspage_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newspage',
            old_name='intro',
            new_name='short_description',
        ),
    ]
