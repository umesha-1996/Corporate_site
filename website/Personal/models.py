from django.db import models
from wagtail.models import TranslatableMixin,Page
from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.fields import StreamField
from wagtail.admin.panels import FieldPanel

from News.models import NewsIndexPage

class product_block(blocks.StructBlock):
    product_image = ImageChooserBlock(required=True)
    product_name = blocks.CharBlock(required=True)
    product_url = blocks.URLBlock(blank=False, null=False)

class card_block(blocks.StructBlock):
    card_image = ImageChooserBlock(required=True)
    card_title = blocks.CharBlock(required=True)
    card_description = blocks.TextBlock(required=True)
    card_url = blocks.URLBlock(blank=False, null=False)

class announcement_block(blocks.StructBlock):
    announcement_image = ImageChooserBlock(required=True)
    announcement = blocks.CharBlock(required=True)
    announcement_url = blocks.URLBlock(blank=False, null=False)

class persional(Page):
    def get_context(self, request):
        context = super().get_context(request)

        news_index = NewsIndexPage.objects.live().first()
        if news_index:
            news_items = [page.specific for page in news_index.get_children().live().order_by('-first_published_at')[:4]]
        else:
            news_items = []

        context['news_items'] = news_items
        return context

    products = StreamField(
        [
            ('product', product_block())
        ],
        use_json_field=True,
        blank=True
    )

    cards = StreamField(
        [
            ('card', card_block())
        ],
        use_json_field=True,
        blank=True
    )

    announcements = StreamField(
        [
            ('announcement', announcement_block())
        ],
        use_json_field=True,
        blank=True
    )

    content_panels = Page.content_panels + [
        FieldPanel("products"),
        FieldPanel("cards"),
        FieldPanel("announcements")
    ]

    