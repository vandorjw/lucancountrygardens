from django.contrib import admin
from product.models import Category, Product, ProductImage

class ProductImage_Inline(admin.StackedInline):
    model = ProductImage
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        "slug": ("name",),
    }

    list_per_page = 25

    list_display = (
        '__str__',
        'is_active',
    )
    inlines = [ ProductImage_Inline, ]

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        "slug": ("name",),
    }

    list_per_page = 25

    list_display = (
        '__str__',
        'is_active',
    )

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
