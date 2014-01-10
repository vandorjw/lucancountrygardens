from datetime import date
from django.db import models
from django.core.urlresolvers import reverse

class About(models.Model):
    name = models.CharField( max_length=255, unique=True )
    slug = models.SlugField( max_length=255, unique=True )
    image = models.ImageField(upload_to="AboutImages/", blank=True, null=True)
    short_content = models.TextField( blank=True )
    sort = models.IntegerField( default=0, unique=True )
    is_active = models.BooleanField( default=True )
    meta_description = models.CharField( max_length=300, blank=True )
    meta_keywords = models.CharField( max_length=300, blank=True )

    class Meta:
        app_label = 'about'
        ordering = ['sort','name']
        verbose_name_plural = "about"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('about:about_detail', kwargs={'slug':self.slug})
        

class ArticleSection(models.Model):
    about = models.ForeignKey('About')
    sort = models.IntegerField( default=0, unique=True)
    image = models.ImageField(upload_to="AboutImages/", blank=True, null=True)
    image_caption = models.CharField( max_length=255, blank=True )
    section_header = models.CharField( max_length=255 )
    article_section = models.TextField()
    
    class Meta:
        app_label = 'about'
        ordering = ['sort']

    def __str__(self):
            return '%s, %s' % (self.about, self.section_header)
