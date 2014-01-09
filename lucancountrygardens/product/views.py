from django.views import generic
from product.models import Category, Product 

class CategoryListView(generic.ListView):
    queryset = Category.objects.filter(is_active=True).filter(parent=None)

class CategoryDetailView(generic.DetailView):
    model = Category

    def get_context_data(self, **kwargs):
        context = super(CategoryDetailView, self).get_context_data(**kwargs)
        context['subcategories'] = self.object.category_set.all()
        context['category_products'] = self.object.product_set.filter(is_active=True)
        return context

class ProductListView(generic.ListView):
    queryset = Product.objects.filter(is_active=True)

class ProductDetailView(generic.DetailView):
    model = Product

