from django.shortcuts import render
from django.views import View

class ProductView(View):
    def get(self, request):
        return render(request, 'products/list.html',{
          'topwears':123,
        })