from django.views import generic
from about.models import About

class AboutDetailView(generic.DetailView):
    model = About

    def get_context_data(self, **kwargs):
        context = super(AboutDetailView, self).get_context_data(**kwargs)
        context['sections'] = self.object.articlesection_set.all()
        return context
    

class AboutListView(generic.ListView):
    queryset = About.objects.filter(is_active=True)
