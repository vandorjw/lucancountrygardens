from django.contrib.sitemaps import Sitemap

from about.models import About
from gallery.models import Gallery
from product.models import Product
from product.models import Category

class GallerySitemap(Sitemap):
    changefreq = "daily"
    priority = 0.5

    def items(self):
        return Gallery.objects.filter(is_active=True)


class ProductSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.5

    def items(self):
        return Product.objects.filter(is_active=True)


class CategorySitemap(Sitemap):
    changefreq = "daily"
    priority = 0.5

    def items(self):
        return Category.objects.filter(is_active=True)


class AboutSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.5

    def items(self):
        return About.objects.all()

