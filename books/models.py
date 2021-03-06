from django.db import models

from modelcluster.fields import ParentalKey
from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core import blocks
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, InlinePanel, MultiFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.images.blocks import ImageChooserBlock
from wagtail.search import index

# Create your models here.

class Series(models.Model):
    """A representation of a book series."""
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    def __str__(self):
        return self.name

class Genre(models.Model):
    """A representation of a genre."""
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    def __str__(self):
        return self.name

class PenName(models.Model):
    """A representation of an author's pen name."""
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    def __str__(self):
        return self.name

# The ABSTRACT model for Buy Links, with panels
class BuyLink(models.Model):
    vendor_name = models.CharField(max_length=255)
    link_address = models.URLField("URL", blank=True)
    panels = [
        FieldPanel('vendor_name'),
        FieldPanel('link_address'),
    ]
    class Meta:
        abstract = True

# Set the item as keyed to the page.
class BookPageBuyLinks(Orderable, BuyLink):
    page = ParentalKey('books.BookPage', on_delete=models.CASCADE, related_name='buy_links')

# Abstract model for book reviews, with panels:
class BookReview(models.Model):
    reviewer = models.CharField(max_length=255, blank=True)
    review_venue = models.CharField(max_length=255, blank=True)
    review_text = models.TextField(blank=True)
    review_link = models.URLField(blank=True)

    panels = [
        FieldPanel('reviewer'),
        FieldPanel('review_venue'),
        FieldPanel('review_text', classname="full"),
        FieldPanel('review_link'),
    ]

    class Meta:
        abstract = True
    
class BookPageReviewBox(Orderable, BookReview):
    page = ParentalKey('books.BookPage', on_delete=models.CASCADE, related_name='book_reviews')

class BookPage(Page):
    """A page for an author's book."""
    book_title = models.CharField(max_length=200)
    author = models.ForeignKey(PenName, on_delete=models.SET_NULL, null=True)
    series = models.ForeignKey(Series, blank=True, null=True, on_delete=models.SET_NULL)
    release_date = models.DateField(blank=True)
    description = RichTextField(blank=True)

    content_panels = Page.content_panels + [
    InlinePanel('buy_links', label="Buy Links"),
    InlinePanel('book_reviews', label="Book Reviews"),
  ]

class BooksIndexPage(Page):
    intro = RichTextField(blank=True)
    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full")
    ]
