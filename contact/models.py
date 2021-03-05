from django.conf import settings
from django.db import models
from django import forms
from django.core.mail import send_mail
from django.shortcuts import render

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel

   
class ContactPage(Page):
    """A custom contact page with contact form."""
    body = RichTextField(blank=True)
    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full")
    ]

    def serve(self, request):
        from contact.forms import ContactForm
        form = ContactForm(request.POST)
        if form.is_valid():
            # Clean the data
            senders_name = form.cleaned_data['your_name']
            senders_email = form.cleaned_data['your_email']
            message_subject = form.cleaned_data['subject']
            message = form.cleaned_data['your_message']
            #Process the form info to get it ready for send_mail
            subject_line = f"""New message from {WAGTAIL_SITE_NAME} contact form: 
            {message_subject}"""
            message_body = f"""You have recieved the following message from
            your website, {WAGTAIL_SITE_NAME}:\n\nSender's Name: {senders_name}\n\n
            Sender's Email:{senders_email}\n\nSubject:{message_subject}\n\n
            Message Body: {message}"""
            # And send
            # Add a try/except block with errors!
            send_mail(subject_line, message_body, senders_email, CONTACT_EMAIL)
        else:
            form = ContactForm()
        return render(request, 'contact/contact_page.html', {
            'page':self,
            'form':form,
        })

