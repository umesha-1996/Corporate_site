
from wagtail.models import Page
from django.shortcuts import render


def global_search(request):
    query = request.GET.get("query", "")
    results = []

    if query:
        results = Page.objects.live().autocomplete(query)

    return render(request, "search/search.html", {
        "query": query,
        "results": results,
    })
