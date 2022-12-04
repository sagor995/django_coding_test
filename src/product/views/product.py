from django.views import generic
from django.shortcuts import render
from product.models import Variant, Product, ProductVariant

from django.views import View

class CreateProductView(generic.TemplateView):
    template_name = 'products/create.html'

    def get_context_data(self, **kwargs):
        context = super(CreateProductView, self).get_context_data(**kwargs)
        variants = Variant.objects.filter(active=True).values('id', 'title')
        context['product'] = True
        context['variants'] = list(variants.all())
        return context

class ProductView(View):
    def get(self, request):
        #products = Product.objects.values('id','title','description')
        product_varient = ProductVariant.objects.values('id','variant_title')
        print(product_varient)
        return render(request, 'products/list.html'
        # ,{
        #     'products':products,
        # }
        )
