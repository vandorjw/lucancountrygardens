from django.db import models

class Slide(models.Model):
    image = models.ImageField(upload_to="jumbotron/", blank=True, null=True)
    caption = models.CharField( max_length=255, blank=True )
    sort = models.IntegerField( default=0 )
    is_active = models.BooleanField( default=True )
    
    class Meta:
        app_label = 'jumbotron'
        ordering = ['sort']

    def __str__(self):
        return self.caption
