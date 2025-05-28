from wagtail.snippets.models import register_snippet
from wagtail.admin.panels import FieldPanel
from django.db import models
from wagtail.models import (
    TranslatableMixin,
)
from wagtail.fields import StreamField
from wagtail import blocks

@register_snippet
class Footer(TranslatableMixin, models.Model):
    # Row 1
    logo = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Comapny Logo",
    )

    visit_us = models.CharField(max_length=255)

    visit_us_icon = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Visit Us Icon",
    )
    visit_us = models.CharField(max_length=255)


    call_us_icon = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Call Us Icon",
    )

    call_us = StreamField([
        ("contact", blocks.StructBlock([
            ("country", blocks.CharBlock()),
            ("contact_no", blocks.CharBlock()),
        ]))
    ], blank=True, use_json_field=True, help_text="Contact Details")

    write_to_us_icon = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Write To Us Icon",
    )
    write_to_us = models.CharField(max_length=255)

    # Row 2
    introduction = models.TextField()
    about = models.CharField(max_length=255)
    reports = models.CharField(max_length=255)
    faqs = models.CharField(max_length=255)

    # Row 3: Socials
    linkedin_icon = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="LinkedIn Icon",
    )
    linkedin_url = models.URLField(blank=True)

    youtube_icon = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Youtube Icon",
    )
    youtube_url = models.URLField(blank=True)

    twitter_icon = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Twitter Icon",
    )
    twitter_url = models.URLField(blank=True)

    # Row 4
    copyright_text = models.CharField(
        max_length=255
    )

    panels = [
        FieldPanel("logo"),
        FieldPanel("visit_us_icon"),
        FieldPanel("visit_us"),
        FieldPanel("call_us_icon"),
        FieldPanel("call_us"),
        FieldPanel("write_to_us_icon"),
        FieldPanel("write_to_us"),
        FieldPanel("introduction"),
        FieldPanel("about"),
        FieldPanel("reports"),
        FieldPanel("faqs"),
        FieldPanel("linkedin_icon"),
        FieldPanel("linkedin_url"),
        FieldPanel("youtube_icon"),
        FieldPanel("youtube_url"),
        FieldPanel("twitter_icon"),
        FieldPanel("twitter_url"),
        FieldPanel("copyright_text"),
    ]

    # api snipeet ekkne dala thiyenne, admin panel eke snippet menu ek click krama model name eka penwana nama (verbose_name_plural)
    # translation 
    class Meta(TranslatableMixin.Meta):
        verbose_name_plural = "footer"
        
    # table ekt record ekk danmame record ek penwan thana (table eke), mokkd penwanna ona nama.
    def __str__(self):
        return "Footer"

