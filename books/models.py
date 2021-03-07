from django import forms
from django.db import models

from modelcluster.fields import ParentalKey, ParentalManyToManyField
from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core import blocks
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, InlinePanel, MultiFieldPanel, PageChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.images.models import Image
from wagtail.search import index

from django.utils.text import slugify  

# Create your models here.

class Genre(models.Model):
    """A representation of a genre."""
    name = models.CharField(max_length=200)

    def save(self, *args, **kwargs): 
        self.slug = slugify(self.name) 
        super(Genre, self).save(*args, **kwargs) 

    def __str__(self):
        return self.name

class ContentWarning(models.Model):
    """A representatation of a content warning."""
    warning_name = models.CharField(max_length=200)
    warning_slug = models.SlugField(max_length=200)

    def __str__(self):
        return self.warning_name

class AuthorPage(Page):
    """A representation of an author's pen name."""
    author_pen_name = models.CharField(max_length=200)
    author_bio = RichTextField()
    author_photo = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.SET_NULL, related_name='+', null=True, blank=True
    )

    content_panels = Page.content_panels + [
        FieldPanel('author_pen_name'),
        FieldPanel('author_bio'),
        ImageChooserPanel('author_photo'),
    ]

class SeriesPage(Page):
    """A page to represent a book series."""
    series_name = models.CharField(max_length=200)
    total_books = models.IntegerField()
    series_description = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('series_name'),
        FieldPanel('series_description'),
        FieldPanel('total_books'),
    ]

### The following models are displayed on the Books Page ###
# The ABSTRACT model for Buy Links, with panels

class BuyLink(models.Model):
    # An individual buy_link for a book.
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

### Book Page ###
class BookPage(Page):
    """A page for an individual book."""
    book_title = models.CharField(max_length=200)
    author = models.ForeignKey(
        'wagtailcore.Page', on_delete=models.SET_NULL, blank=True, null=True, related_name='+')
    series = models.ForeignKey(
        'wagtailcore.Page', on_delete=models.SET_NULL, blank=True, null=True, related_name='+')
    release_date = models.DateField(blank=True, null=True)
    genre = models.ManyToManyField('books.Genre', blank=True)
    description = RichTextField(blank=True)
    content_warnings = models.ManyToManyField('books.ContentWarning', blank=True)
    cover_image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.SET_NULL, related_name='+', null=True, blank=True)
    other_text = RichTextField(blank=True)
    # Add content panels
    content_panels = Page.content_panels + [
        FieldPanel('book_title', classname="full"),
        PageChooserPanel('author', 'books.AuthorPage'),
        PageChooserPanel('series', 'books.SeriesPage'),
        FieldPanel('release_date'),
        FieldPanel('genre'),
        FieldPanel('description', classname="full"),
        ImageChooserPanel('cover_image'),
        FieldPanel('content_warnings'),
        FieldPanel('other_text'),
        InlinePanel('buy_links', label="Buy Links"),
        InlinePanel('book_reviews', label="Book Reviews"),
    ]

class BooksIndexPage(Page):
    intro = RichTextField(blank=True)
    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full")
    ]
