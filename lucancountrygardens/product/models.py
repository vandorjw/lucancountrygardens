from django.db import models
from django.core.urlresolvers import reverse

class Category(models.Model):
    parent = models.ForeignKey('self', null=True, blank=True )
    name = models.CharField( max_length=255, unique=True )   
    slug = models.SlugField( max_length=255, unique=True )  
    description = models.TextField( blank=True)
    sort = models.IntegerField( unique=True, max_length=2, default=0 )  
    meta_description = models.CharField( max_length=255, blank=True )
    meta_keywords = models.CharField( max_length=255, blank=True )     
    is_active = models.BooleanField( default=True )    
    image = models.ImageField( upload_to="images/", blank=True, null=True )

    class Meta:
        app_label = 'product'
        ordering = ['sort']
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name

    def _recurse_for_parents(self, cat_obj):
        p_list = []
        if cat_obj.parent_id:
            p = cat_obj.parent
            p_list.append(p)
            if p != self:
                more = self._recurse_for_parents(p)
                p_list.extend(more)
        if cat_obj == self and p_list:
            p_list.reverse()
        return p_list

    def get_absolute_url(self):
        parents = self._recurse_for_parents(self)
        slug_list = [cat.slug for cat in parents]
        if slug_list:
            slug_list = "/".join(slug_list) + "/"
        else:
            slug_list = ""
        return reverse('product:category_detail',
            kwargs={'parent_slugs' : slug_list, 'slug' : self.slug})


class Product(models.Model):
    name = models.CharField( max_length=255 )
    slug = models.SlugField( max_length=255, unique=True )  
    category = models.ForeignKey('Category', null=True, blank=True )
    meta_description = models.CharField( max_length=255, blank=True )
    meta_keywords = models.CharField( max_length=255, blank=True )                
    is_active = models.BooleanField( default=True )    
    is_featured = models.BooleanField( default=False )    
    price = models.DecimalField( max_digits=8, decimal_places=2 )
    description = models.TextField( blank=True)

    class Meta:
        app_label = 'product'
        ordering = ['name']
                
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product:product_detail', kwargs={'slug':self.slug})


class ProductImage(models.Model):
    product = models.ForeignKey('Product')
    image = models.ImageField( upload_to="images/", blank=True, null=True)
    caption = models.CharField( max_length=255, blank=True)
    sort = models.IntegerField( default=0 )

    class Meta:
        app_label = 'product'
        ordering = ['sort']
    
    def __str__(self):
            return self.caption
  



