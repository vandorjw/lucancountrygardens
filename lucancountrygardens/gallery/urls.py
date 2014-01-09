from django.conf.urls import url, patterns, include
from gallery import views

urlpatterns = patterns("",
    url(
        regex=r"^$",
        view=views.GalleryListView.as_view(),
        name='gallery_list',
    ),
    url(
        regex=r"^(?P<slug>[-\w]+)/$",
        view=views.GalleryDetailView.as_view(),
        name="gallery_detail",
    ),
)
