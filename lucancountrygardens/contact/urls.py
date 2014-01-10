from django.conf.urls import url, patterns, include
from contact import views

urlpatterns = patterns("",
    url(
        regex=r"^$",
        view=views.ContactView.as_view(),
        name='contact_page',
    ),
)
