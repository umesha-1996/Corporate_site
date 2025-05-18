from django.db import models
from django.forms import ValidationError
from wagtail.admin.panels import FieldPanel
from wagtail.admin.panels import (
    FieldPanel,
)
from wagtail.models import Page
from django.contrib import messages
from django.shortcuts import render, redirect

from .utils import validate_international_phone


class ContactUsPage(Page):
    youtube_url = models.URLField(help_text="Paste YouTube video URL", blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('youtube_url'),
    ]

    def serve(self, request):
        if request.method == 'POST':
            # Get data from POST
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            phone = request.POST.get('phone')
            extension = request.POST.get('extension', '')
            postal_code = request.POST.get('postal_code', '')
            email = request.POST.get('email')
            message = request.POST.get('message')

            # Validate phone number
            try:
                validate_international_phone(phone)
            except ValidationError as e:
                messages.error(request, str(e))
                return render(request, self.get_template(request), {
                    'page': self,
                    'form_data': request.POST,
                })

            # Save to database
            ContactSubmission.objects.create(
                page=self,
                first_name=first_name,
                last_name=last_name,
                phone=phone,
                extension=extension,
                postal_code=postal_code,
                email=email,
                message=message,
            )

            messages.success(request, "Thank you! Your message has been submitted.")
            return redirect(request.path)

        return render(request, self.get_template(request), {
            'page': self,
        })


# This model stores the user submissions
class ContactSubmission(models.Model):
    page = models.ForeignKey(ContactUsPage, on_delete=models.CASCADE, related_name='submissions')
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    extension = models.CharField(max_length=10, blank=True)
    postal_code = models.CharField(max_length=20, blank=True)
    email = models.EmailField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.email}"