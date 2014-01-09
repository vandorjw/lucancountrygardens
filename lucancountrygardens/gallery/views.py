from django.views import generic
from gallery.models import Gallery

class GalleryDetailView(generic.DetailView):
    model = Gallery

class GalleryListView(generic.ListView):
    queryset = gallery.objects.filter(is_active=True)

