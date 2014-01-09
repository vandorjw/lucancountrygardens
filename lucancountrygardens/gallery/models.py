from django.db import models
from django.core.urlresolvers import reverse

class Gallery(models.Model):
    name = models.CharField( max_length=255, unique=True )
    slug = models.SlugField( max_length=255, unique=True )
    description = models.TextField( blank=True )
    meta_description = models.CharField( max_length=255, blank=True )
    meta_keywords = models.CharField( max_length=255, blank=True )
    is_active = models.BooleanField( default=True )

    class Meta:
        app_label = 'gallery'
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('gallery:gallery_detail', kwargs={'slug':self.slug})
        

class GalleryImage(models.Model):
    product = models.ForeignKey('Gallery')
    image = models.ImageField(upload_to="gallery/", blank=True, null=True)
    caption = models.CharField( max_length=255, blank=True)
    sort = models.IntegerField( default=0, unique=True )

    class Meta:
        app_label = 'gallery'
        ordering = ['sort']
    
    def __str__(self):
        return self.caption
