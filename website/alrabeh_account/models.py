from django.db import models
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel
from wagtail.search import index
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, InlinePanel
from modelcluster.models import ClusterableModel
from modelcluster.fields import ParentalKey


class AlrbehAccountIndexPage(Page):
    max_count = 1
    mani_title = models.CharField(max_length=200)
    short_description = models.CharField(max_length=255)

    content_panels = Page.content_panels + [
        FieldPanel('mani_title'),
        FieldPanel('short_description'),
        InlinePanel("account_features", label="Features")
    ]

    search_fields = Page.search_fields + [
        index.AutocompleteField("mani_title", partial_match=True),
        index.AutocompleteField("short_description", partial_match=True)
    ]


class AlrbehAccountPage(Page):
    parent_page_types = ['alrabeh_account.AlrbehAccountIndexPage']
    subpage_types = []

    short_title = models.CharField(max_length=255, default='Default title')
    body = RichTextField(blank=True)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = Page.content_panels + [
        FieldPanel('short_title'),
        FieldPanel('body'),
        FieldPanel('image'),
    ]

    search_fields = Page.search_fields + [
        index.AutocompleteField("short_title", partial_match=True),
        index.AutocompleteField("body", partial_match=True)
    ]


class AccountFeature(ClusterableModel):
    page = ParentalKey(AlrbehAccountIndexPage, related_name="account_features", on_delete=models.CASCADE)
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