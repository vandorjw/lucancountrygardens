from django.contrib import admin
from django.contrib.admin import BooleanFieldListFilter
from about.models import About, ArticleSection

class ArticleSection_Inline(admin.StackedInline):
    model = ArticleSection
    extra = 1

class AboutAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        "slug": ("name",),
    }

    list_per_page = 25

    list_display = (
        '__str__',
        'is_active',
        'sort',
    )

    list_filter = (
        ('is_active', BooleanFieldListFilter),
    )

    search_fields = ['slug', 'name',]
    inlines = [ ArticleSection_Inline, ]

admin.site.register(About, AboutAdmin)
