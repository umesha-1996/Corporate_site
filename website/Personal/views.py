from django.shortcuts import render

def personal_page(request):
    return render(request, 'personal_page.html')