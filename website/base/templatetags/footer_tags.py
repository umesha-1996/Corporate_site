from django import template
from base.models import Footer

# How Django knows you're creating custom template tags
register = template.Library()

@register.inclusion_tag('includes/footer.html', takes_context=True)
def render_footer(context):
    footer = Footer.objects.first()
    return {'footer': footer}
