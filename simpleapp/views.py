from django.views.generic import ListView
from django.views.generic import DetailView
from datetime import datetime
from .models import Product
from .filters import ProductFilter


class ProductList(ListView):
    model = Product
    ordering = 'name'
    template_name = 'simpleapp/products.html'
    context_object_name = 'products'
    paginate_by = 2

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = ProductFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        contex = super().get_context_data()
        contex['next_sale'] = "Sales is tommorow!"
        contex['filterset'] = self.filterset
        return contex


class ProductDetail(DetailView):
    model = Product
    template_name = 'simpleapp/product.html'
    context_object_name = 'product'
