from django.conf.urls import url, patterns, include
from about import views

urlpatterns = patterns("",
    url(
        regex=r"^$",
        view=views.AboutListView.as_view(),
        name='about_list',
    ),
    url(
        regex=r"^(?P<slug>[-\w]+)/$",
        view=views.AboutDetailView.as_view(),
        name="about_detail",
    ),
)
