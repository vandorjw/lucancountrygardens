from django.views.generic import TemplateView
        
class RobotPageView(TemplateView):
    template_name="robots.txt"
    content_type='text/plain'
    
class HumanPageView(TemplateView):
    template_name="humans.txt"
    content_type='text/plain'

class GooglePageView(TemplateView):
    template_name="google25e8e23e2bfc7d2c.html"
    content_type='text/plain'
