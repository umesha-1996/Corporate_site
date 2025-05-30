# Generated by Django 5.1 on 2025-05-10 05:55

import wagtail.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_create_homepage'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='cta',
            field=wagtail.fields.StreamField([('cta_button', 2)], blank=True, block_lookup={0: ('wagtail.blocks.CharBlock', (), {}), 1: ('wagtail.blocks.URLBlock', (), {}), 2: ('wagtail.blocks.StructBlock', [[('text', 0), ('url', 1)]], {})}, help_text='Call-to-action buttons'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='hero_images',
            field=wagtail.fields.StreamField([('image', 0)], blank=True, block_lookup={0: ('wagtail.images.blocks.ImageChooserBlock', (), {})}, help_text='Hero banner images'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='highlights',
            field=wagtail.fields.StreamField([('highlight', 2)], blank=True, block_lookup={0: ('wagtail.blocks.CharBlock', (), {}), 1: ('wagtail.blocks.TextBlock', (), {}), 2: ('wagtail.blocks.StructBlock', [[('title', 0), ('description', 1)]], {})}, help_text='Highlighted services/products'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='stats',
            field=wagtail.fields.StreamField([('stat', 1)], blank=True, block_lookup={0: ('wagtail.blocks.CharBlock', (), {}), 1: ('wagtail.blocks.StructBlock', [[('label', 0), ('value', 0)]], {})}, help_text='Key stats or achievements'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='tagline',
            field=wagtail.fields.RichTextField(blank=True, help_text='Company tagline or mission statement'),
        ),
    ]
