from django.contrib import admin
from .models import *

from .models import (
    Variant,
    Product,
    ProductImage,
    ProductVariant,
    ProductVariantPrice
)

# Register your models here.
@admin.register(Product)
class ProductAdminModel(admin.ModelAdmin):
    list_display = ['title','sku','description','created_at','updated_at']

@admin.register(ProductImage)
class ProductImageAdminModel(admin.ModelAdmin):
    list_display = ['file_path','created_at','updated_at']

@admin.register(ProductVariant)
class ProductVariantAdminModel(admin.ModelAdmin):
    list_display = ['variant_title','created_at','updated_at']

@admin.register(ProductVariantPrice)
class ProductVariantPriceAdminModel(admin.ModelAdmin):
    list_display = ['product_variant_one','product_variant_two','product_variant_three',
    'price','stock','created_at','updated_at']

@admin.register(Variant)
class VariantAdminModel(admin.ModelAdmin):
    list_display = ['title','description','created_at','updated_at']