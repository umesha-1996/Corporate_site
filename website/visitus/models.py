from django.db import models
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.fields import RichTextField
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel


class VisitPage(Page):
    template = "visitus/visit_page.html"
    parent_page_types = ['home.HomePage'] 

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)

        branches_page = BranchesPage.objects.live().first()
        atm_page = AtmPage.objects.live().first()

        context['visit_us_items'] = []

        if branches_page:
            context['visit_us_items'].append({'page': branches_page, 'pagetitle': 'branch'})
        if atm_page:
            context['visit_us_items'].append({'page': atm_page, 'pagetitle': 'atm'})
        return context

    class Meta:
        verbose_name = "Visit Us Page"
        verbose_name_plural = "Visit Us Pages"

class BranchLocation(ClusterableModel):
    city_page = ParentalKey('BranchCityPage', related_name='locations')
    is_available_ladies_section = models.BooleanField(default=False)
    title = models.CharField(max_length=255, help_text="Main Street Branch")
    atm_machine_count = models.IntegerField(default=0)
    phone = models.CharField(max_length=20, blank=True, null=True)
    opening_time = models.TextField(blank=True, null=True)
    close_time = models.TextField(blank=True, null=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)

    panels = [
        FieldPanel('is_available_ladies_section'),
        FieldPanel('title'),
        FieldPanel('atm_machine_count'),
        FieldPanel('phone'),
        FieldPanel('opening_time'),
        FieldPanel('close_time'),
        MultiFieldPanel(
            [
                FieldPanel('latitude'),
                FieldPanel('longitude'),
            ],
            heading="Map Coordinates"
        ),
    ]

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Branch Location"
        verbose_name_plural = "Branch Locations"
        ordering = ['title']

class BranchCityPage(Page, ClusterableModel):
    template = "visitus/branch_city_page.html"
    parent_page_types = ['BranchesPage']
    subpage_types = [] 

    city_name = models.CharField(max_length=255)

    content_panels = Page.content_panels + [
        FieldPanel('city_name'),
        InlinePanel('locations', label="Branch Locations", min_num=1), 
    ]

    def __str__(self):
        return self.city_name

    class Meta:
        verbose_name = "Branch City Page"
        verbose_name_plural = "Branch City Pages"
        ordering = ['city_name']


class BranchesPage(Page):
    template = "visitus/branches_page.html"
    parent_page_types = ['VisitPage'] 
    subpage_types = ['BranchCityPage'] 

    item_title = models.CharField(max_length=255)
    item_icon = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Branch Icon",
    )
    content_panels = Page.content_panels + [
        FieldPanel('item_title'),
        FieldPanel('item_icon'),
    ]


    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
      
        context['cities'] = self.get_children().live().specific()
        return context

    class Meta:
        verbose_name = "Branches Page"
        verbose_name_plural = "Branches Pages"

class AtmLocation(ClusterableModel):
    city_page = ParentalKey('AtmCityPage', related_name='locations')
    title = models.CharField(max_length=255, help_text="Main Street Branch")
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)

    panels = [
        FieldPanel('title'),
        MultiFieldPanel(
            [
                FieldPanel('latitude'),
                FieldPanel('longitude'),
            ],
            heading="Map Coordinates"
        ),
    ]

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "ATM Location"
        verbose_name_plural = "ATM Locations"
        ordering = ['title']

class AtmCityPage(Page, ClusterableModel):
    template = "visitus/atm_page.html"
    parent_page_types = ['AtmPage']
    subpage_types = [] 

    city_name = models.CharField(max_length=255)

    content_panels = Page.content_panels + [
        FieldPanel('city_name'),
        InlinePanel('locations', label="Atm Locations", min_num=1), 
    ]

    def __str__(self):
        return self.city_name

    class Meta:
        verbose_name = "Branch City Page"
        verbose_name_plural = "Branch City Pages"
        ordering = ['city_name']

class AtmPage(Page):
    template = "visitus/atm_page.html"
    parent_page_types = ['VisitPage'] 
    subpage_types = ['AtmCityPage'] 

    item_title = models.CharField(max_length=255)
    item_icon = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="ATM Icon",
    )
    content_panels = Page.content_panels + [
        FieldPanel('item_title'),
        FieldPanel('item_icon'),
    ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
      
        context['cities'] = self.get_children().live().specific()
        return context
    
    class Meta:
        verbose_name = "ATM Page"
        verbose_name_plural = "ATM Pages"