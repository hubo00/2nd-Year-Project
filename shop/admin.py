from django.contrib import admin
from .models import Category, Product, subCategory

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','name_alt','slug','category','price','description','stock','available','created','updated']
    list_editable = ['price','slug','stock','available']
    list_per_page = 20
    if Product.name_alt:
        prepopulated_fields = {'slug': ('name','name_alt')}
    else:
        prepopulated_fields = {'slug': ('name',)}
admin.site.register(Product,ProductAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'description', 'image']
    list_editable = ['description', 'image']
    list_per_page = 20
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Category,CategoryAdmin)

class subCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'description', 'image']
    list_editable = ['description']
    list_per_page = 20
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(subCategory, subCategoryAdmin)