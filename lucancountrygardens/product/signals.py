from django.db import models
from haystack import signals
from .models import Product

class ProductSignalProcessor(signals.BaseSignalProcessor):
    def setup(self):
        models.signals.post_save.connect(self.handle_save, sender=Product)
        models.signals.post_delete.connect(self.handle_delete, sender=Product)

    def teardown(self):
        models.signals.post_save.disconnect(self.handle_save, sender=Product)
        models.signals.post_delete.disconnect(self.handle_delete, sender=Product)
