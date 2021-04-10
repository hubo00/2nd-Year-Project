from django.contrib import admin
from .models import Category, Product, subCategory

# Class for Product Admin
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','name_alt','slug','category','price','description','stock','available','created','updated']
    list_editable = ['price','slug','stock','available']
    list_per_page = 20
    # If the product has an alternative name, display the slug field as name and alt_name
    if Product.name_alt:
        prepopulated_fields = {'slug': ('name','name_alt')}
    # Else if the product doesn't have an alt name, display the slug as just the name
    else:
        prepopulated_fields = {'slug': ('name',)}
admin.site.register(Product,ProductAdmin)

# Class for Category Admin
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'description', 'image']
    list_editable = ['description', 'image']
    list_per_page = 20
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Category,CategoryAdmin)

# Class for Subcategory Admin
class subCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'description', 'image']
    list_editable = ['description']
    list_per_page = 20
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(subCategory, subCategoryAdmin)