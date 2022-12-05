from django.views import generic
from django.shortcuts import render
from product.models import *

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
        products = Product.objects.values()

        product = Product.objects.all()
        productss = []
        print("###")
        for pro in product:
            dic = {}
            dic['title'] = pro.title
            dic['description'] = pro.description
            dic['created_at'] = pro.created_at
            product_varient_prices = ProductVariantPrice.objects.filter(product_id=pro).all()
            varients = []
            for pvp in product_varient_prices:
                dic2 = {} 
                price = pvp.price
                stock = pvp.stock
                pvp1 = pvp.product_variant_one.variant_title
                pvp2 = pvp.product_variant_two.variant_title
                pvp3 = pvp.product_variant_three.variant_title

                dic2['price'] = price
                dic2['stock'] = stock
                dic2['pvp'] = pvp1+" / "+pvp2+" / "+pvp3
                varients.append(dic2)
            dic['varient'] = varients
            productss.append(dic)
        print(productss)
        print("#####")
                #varients.append(dic2)
            #dic['varient'] = varients
            #productss.append(dic)
            #print(productss)
        return render(request, 'products/list.html',{'products':productss,})
