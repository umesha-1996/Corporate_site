from django.db import models
from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.admin.panels import FieldPanel
from wagtail.search import index

class benifite_block(blocks.StructBlock):
    benifite_image = ImageChooserBlock(required=True)
    benifite_title = blocks.CharBlock(required=True)
    benifite_description = blocks.CharBlock(required=True)

class GoldIndexPage(Page):
    subpage_types = ['gold_account.GoldPage']
    max_count = 1

class GoldPage(Page):
    parent_page_types = ['gold_account.GoldIndexPage']
    subpage_types = []

    gold_account_icon = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Gold Account Icon",
    )
    short_title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    benifites = StreamField(
        [
            ('benifite', benifite_block())
        ],
        use_json_field=True,
        blank=True
    )

    content_panels = Page.content_panels + [
        FieldPanel('gold_account_icon'),
        FieldPanel('short_title'),
        FieldPanel('price'),
        FieldPanel('benifites')
    ]

    search_fields = Page.search_fields + [
        index.AutocompleteField("short_title", partial_match=True),
        index.AutocompleteField("price", partial_match=True),
        index.AutocompleteField("benifites", partial_match=True),
    ]