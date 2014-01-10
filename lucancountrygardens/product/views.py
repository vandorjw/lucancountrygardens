from django.views import generic
from product.models import Category, Product 

class CategoryListView(generic.ListView):
    model = Category

    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        context['featured_products'] = Product.objects.filter(is_featured=True)
        context['root_categories'] = Category.objects.filter(is_active=True).filter(parent=None)
        return context
    

class CategoryDetailView(generic.DetailView):
    model = Category

    def get_context_data(self, **kwargs):
        context = super(CategoryDetailView, self).get_context_data(**kwargs)
        context['subcategories'] = self.object.category_set.all()
        context['category_products'] = self.object.product_set.filter(is_active=True)
        return context


class ProductDetailView(generic.DetailView):
    model = Product

