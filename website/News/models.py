from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel
from django.db import models
from wagtail.snippets.models import register_snippet
from wagtail.search import index
from django.core.paginator import Paginator
from django.utils.timezone import now
from wagtail.models import TranslatableMixin,Page

@register_snippet
class NewsCategory(models.Model):
    name = models.CharField(max_length=255, unique=True)

    panels = [
        FieldPanel('name'),
    ]

    def __str__(self):
        return self.name

class NewsIndexPage(Page):

    subpage_types = ['News.NewsPage']
    max_count = 1


    def get_context(self, request):
        context = super().get_context(request)

        posts = NewsPage.objects.live().descendant_of(self).order_by('-date')

        year = request.GET.get('year')
        month = request.GET.get('month')
        category = request.GET.get('category')

        if year:
            posts = posts.filter(date__year=year)
        if month:
            posts = posts.filter(date__month=month)
        if category:
            posts = posts.filter(category__name=category)

        paginator = Paginator(posts, 6)
        page = request.GET.get('page')
        paginated_posts = paginator.get_page(page)

        year_list = posts.dates('date', 'year', order='DESC')
        years = [d.year for d in year_list]
        months = [(i, now().replace(month=i).strftime('%B')) for i in range(1, 13)]
        categories = NewsCategory.objects.all().distinct()

        context.update({
            'posts': paginated_posts,
            'years': years,
            'months': months,
            'categories': categories,
            'query_string': request.GET.urlencode().replace(f'page={page}', '') if page else request.GET.urlencode()
        })
        return context

class NewsPage(Page):
    parent_page_types = ['News.NewsIndexPage']
    subpage_types = []

    date = models.DateField("Post date")
    category = models.ForeignKey(
        NewsCategory,
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='news_pages'
    )
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
        FieldPanel('date'),
        FieldPanel('category'),
        FieldPanel('short_title'),
        FieldPanel('body'),
        FieldPanel('image'),
    ]

    search_fields = Page.search_fields + [
        index.AutocompleteField("date", partial_match=True),
        index.AutocompleteField("category", partial_match=True),
        index.AutocompleteField("short_title", partial_match=True),
        index.AutocompleteField("body", partial_match=True)
    ]
