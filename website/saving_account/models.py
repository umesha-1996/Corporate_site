from django.db import models
from wagtail.models import Page
from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail.search import index
from wagtail.fields import StreamField
from modelcluster.models import ClusterableModel
from modelcluster.fields import ParentalKey

class feature_block(blocks.StructBlock):
    feature_image = ImageChooserBlock(required=True)
    feature_title = blocks.CharBlock(required=True)
    feature_description = blocks.CharBlock(required=True)

class SavingAccountPage(Page):
    main_title = models.CharField(max_length=150)
    short_description = models.CharField(max_length=255)
    features_icon_panel = StreamField(
        [
            ('benifite', feature_block())
        ],
        use_json_field=True,
        blank=True
    )

    content_panels = Page.content_panels + [
        FieldPanel("main_title"),
        FieldPanel("short_description"),
        FieldPanel("features_icon_panel"),
        InlinePanel("account_features", label="Features")
    ]

    search_fields = Page.search_fields + [
        index.AutocompleteField("main_title", partial_match=True),
        index.AutocompleteField("short_description", partial_match=True),
        index.AutocompleteField("account_features", partial_match=True)
    ]

class AccountFeature(ClusterableModel):
    page = ParentalKey(SavingAccountPage, related_name="account_features", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)

    panels = [
        FieldPanel("title"),
        InlinePanel("feature_descriptions", label="Descriptions")
    ]

class FeatureDescription(models.Model):
    feature = ParentalKey(AccountFeature, related_name="feature_descriptions", on_delete=models.CASCADE)
    description = models.TextField()

    panels = [
        FieldPanel("description"),
    ]