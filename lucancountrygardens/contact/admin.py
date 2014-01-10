from django.contrib import admin
from .models import OperationHours

class OperationHoursAdmin(admin.ModelAdmin):
   list_display = (
        'days',
        'value',
    )

admin.site.register(OperationHours, OperationHoursAdmin)
