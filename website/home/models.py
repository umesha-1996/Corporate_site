from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField, StreamField
from wagtail.admin.panels import FieldPanel
from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.admin.panels import FieldPanel


class HeroImageBlock(blocks.StructBlock):
    image = ImageChooserBlock(required=True)
    title = blocks.CharBlock(required=True)
    description = blocks.TextBlock(required=True)

    class Meta:
        template = "home/home_page_image_block.html"
        icon = "image"
        label = "Home Page Image With Text"

class HomePage(Page): 
    home_page_images = StreamField(
        [
            ('home_page_image', HeroImageBlock()),
        ],
        use_json_field=True,
        blank=True
    )

    tagline = RichTextField(blank=True, help_text="Company tagline or mission statement")

    hero_images = StreamField([
        ("image", ImageChooserBlock())
    ], blank=True, use_json_field=True, help_text="Hero banner images")

    who_we_are = StreamField([
        ("highlight", blocks.StructBlock([
            ("title", blocks.CharBlock()),
            ("description", blocks.TextBlock()),
        ]))
    ], blank=True, use_json_field=True, help_text="What we do")

    highlights = StreamField([
        ("Growth", blocks.StructBlock([
            ("title", blocks.CharBlock()),
            ("description", blocks.TextBlock()),
        ]))
    ], blank=True, use_json_field=True, help_text="Growth")

    stats = StreamField([
        ("stat", blocks.StructBlock([
            ("label", blocks.CharBlock()),
            ("value", blocks.CharBlock()),
        ]))
    ], blank=True, use_json_field=True, help_text="Key stats or achievements")

    cta = StreamField([
        ("cta_button", blocks.StructBlock([
            ("text", blocks.CharBlock()),
            ("url", blocks.URLBlock()),
        ]))
    ], blank=True, use_json_field=True, help_text="Call-to-action buttons")

    content_panels = Page.content_panels + [
        FieldPanel("home_page_images"),
        FieldPanel("tagline"),
        FieldPanel("hero_images"),
        FieldPanel("who_we_are"),
        FieldPanel("highlights"),
        FieldPanel("stats"),
        FieldPanel("cta"),
    ]
