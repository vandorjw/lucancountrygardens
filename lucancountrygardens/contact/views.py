from django.views.generic import ListView
from .models import OperationHours

class ContactView(ListView):
    model = OperationHours
    template_name = 'contact/store_hours.html'
