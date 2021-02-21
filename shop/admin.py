from django.contrib import admin
from .models import Category, Product, CatProd

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
admin.site.register(Category,CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','price','description','stock','available','created','updated']
    list_editable = ['price','stock','available']
    list_per_page = 20
admin.site.register(Product,ProductAdmin)

class CatProdAdmin(admin.ModelAdmin):
    list_display = ['category', 'product']
admin.site.register(CatProd, CatProdAdmin)