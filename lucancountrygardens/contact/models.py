from django.db import models

class OperationHours(models.Model):
    days = models.CharField( max_length=255 )
    value = models.CharField( max_length=255 )
    display_order = models.IntegerField( max_length=1, unique=True, default=0 )

    class Meta:
        app_label = 'contact'
        ordering = ['display_order']
        verbose_name_plural = "Operation Hours"

    def __str__(self):
       return self.days
