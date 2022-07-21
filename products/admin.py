from django.contrib import admin
from .models import Product, Brand, Category, ProductImages, Review
# Register your models here.

class ProductImagesInline(admin.TabularInline):
    model = ProductImages

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImagesInline]

admin.site.register(Product,ProductAdmin)
admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(ProductImages)
admin.site.register(Review)