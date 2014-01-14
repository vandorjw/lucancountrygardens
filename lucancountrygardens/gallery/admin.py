from django.contrib import admin
from django.contrib.admin import BooleanFieldListFilter
from sorl.thumbnail.admin import AdminImageMixin

from gallery.models import Gallery
from gallery.models import GalleryImage

class GalleryImage_Inline(AdminImageMixin, admin.TabularInline):
    model = GalleryImage
    extra = 1

class GalleryAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        "slug": ("name",),
    }

    list_per_page = 25

    list_display = (
        '__str__',
    )
    
    search_fields = ['slug', 'name',]
    inlines = [ GalleryImage_Inline, ]


admin.site.register(Gallery, GalleryAdmin)
