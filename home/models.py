from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel


class IndexPage(Page):
  subheading = models.CharField(max_length=140, blank=True)
  summary = models.CharField(max_length=140, blank=True, default='')
  body = RichTextField(blank=True)
  
  content_panels = Page.content_panels + [
  FieldPanel('summary', classname= 'full'),
  FieldPanel('subheading', classname= 'full'),
  FieldPanel('body', classname='full')
  ]

class ProjectPage(Page):
  subheading = models.CharField(max_length=140, blank=True)
  date = models.DateField("Post date")
  clientname = models.CharField(max_length=250)
  body = RichTextField()
  featured_image = models.ForeignKey(
  'wagtailimages.Image',
   null=True,
   blank=True,
   on_delete=models.SET_NULL,
   related_name='+')
  
  content_panels = Page.content_panels + [
  FieldPanel('subheading', classname= 'full'),
  FieldPanel('date'),
  FieldPanel('clientname', classname= 'full'),
  FieldPanel('featured_image'),
  FieldPanel('body', classname='full')
  ]