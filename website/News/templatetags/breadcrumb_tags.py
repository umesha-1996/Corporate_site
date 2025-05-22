from django import template

register = template.Library()

@register.inclusion_tag('News/breadcrumb.html', takes_context=True)
def render_breadcrumbs(context):
    page = context['page']
    return {'page': page}
