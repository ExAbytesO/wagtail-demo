from django.db import models

from wagtail.wagtailcore.models import Page
from wagtail.wagtailadmin.edit_handlers import FieldPanel

class ProjectPage(Page)
  feature_image = models.foreignKey('wagtailimages.Image',
	null= True,
	blank= True,
	on_delete=models.SET_NULL,
	related_name = '-')
  body = RichTextField(blank = True)
  thumbnail_image = models.foreignKey(
  'wagtailimages.Image',
  null = True,
  blank = True
  on_delete = models.SET_NULL,
  related_name = '-')
  
  content_panels = [
    FieldPanel('title'),
	FieldPanel('body', classname = "full"),
	FieldPanel('excerpt'),
	ImageChooserPanel('feature_image'),
	ImageChooserPanel('thumbnail_image'),
  ]
  
class IndexPage(Page):
  pass