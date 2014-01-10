from django.conf.urls import patterns, include, url
from django.contrib import admin
from .sitemap import ProductSitemap, CategorySitemap, GallerySitemap, AboutSitemap
from .views import RobotPageView, HumanPageView, GooglePageView
admin.autodiscover()

sitemaps = {
    'product': ProductSitemap,
    'category': CategorySitemap,
    'gallery': GallerySitemap,
    'about': AboutSitemap,
}

urlpatterns = patterns('',

    url(
        regex=r"^robots\.txt$",
        view=RobotPageView.as_view(),
        name="site_robots",
    ),

    url(
        regex=r"^humans\.txt$",
        view=HumanPageView.as_view(),
        name="site_humans",
    ),

    url(
        regex=r"^google25e8e23e2bfc7d2c\.html$",
        view=GooglePageView.as_view(),
        name="google_webmasters",
    ),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^search/', include('haystack.urls')),
    url(r'^gallery/', include('gallery.urls', namespace='gallery', app_name='gallery')),
    url(r'^about/', include('about.urls', namespace='about', app_name='about')),
    url(r'^', include('product.urls', namespace='product', app_name='product')),
)
