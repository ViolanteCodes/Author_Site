from django.db import models
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from django.conf import settings


class HomePage(Page):
    body = RichTextField(blank=True)
    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
    ]

class LandingPage(Page):
    """A stylish, custom landing page with jumbotron and dual images"""
    jumbotron_background = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.SET_NULL, related_name='+', null=True)
    jumbotron_left_image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.SET_NULL, related_name='+', null=True)
    jumbotron_right_image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.SET_NULL, related_name='+', null=True)
    jumbotron_text = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        ImageChooserPanel('jumbotron_background'),
        ImageChooserPanel('jumbotron_left_image'),
        ImageChooserPanel('jumbotron_right_image'),
        FieldPanel('jumbotron_text', classname="full"),
    ]
