from django.conf.urls import url, patterns
from product.views import CategoryListView, CategoryDetailView, ProductDetailView

urlpatterns = patterns('',
    url(
        r"^categories/$", 
        CategoryListView.as_view(), 
        name="category_list"
    ),
    url(
        r"^product/(?P<slug>[-\w]+)/$",
        ProductDetailView.as_view(), 
        name="product_detail"
    ),
    url(
        r"^(?P<parent_slugs>([-\w]+/)*)?(?P<slug>[-\w]+)/$",
        CategoryDetailView.as_view(),
        name="category_detail"
    ),
)
