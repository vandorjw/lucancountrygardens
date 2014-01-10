from django.views.generic import TemplateView
from product.models import Category
from about.models import About
from gallery.models import Gallery

class HomePageView(TemplateView):
    template_name="home_page.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['root_categories'] = Category.objects.filter(is_active=True).filter(parent=None)
        context['about_pages'] = About.objects.filter(is_active=True)
        context['galleries'] = Gallery.objects.filter(is_active=True).filter(is_featured=True)
        #context['banners'] = _some_model_.objects.filter(is_active=True)
        return context
        

class RobotPageView(TemplateView):
    template_name="robots.txt"
    content_type='text/plain'

    
class HumanPageView(TemplateView):
    template_name="humans.txt"
    content_type='text/plain'


class GooglePageView(TemplateView):
    template_name="google25e8e23e2bfc7d2c.html"
    content_type='text/plain'
