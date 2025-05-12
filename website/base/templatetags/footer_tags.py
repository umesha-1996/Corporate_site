from django import template
from base.models import Footer

register = template.Library()

@register.inclusion_tag('includes/footer.html', takes_context=True)
def render_footer(context):
    footer = Footer.objects.first()
    return {'footer': footer}
