from django.contrib import admin
from .models import Review

class ReviewAdmin(admin.ModelAdmin):
    list_display = ['product',
    'pub_date',
    'user',
    'username',
    'title',
    'content',
    'image_thumbnail',
    'rating']
    list_editable = ['title', 'username', 'content']
    list_per_page = 20
admin.site.register(Review, ReviewAdmin)