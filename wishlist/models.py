from django.db import models
from django.urls import reverse
from accounts.models import CustomUser
from shop.models import Product
from django.utils.text import slugify

class Wishlist(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=120, unique=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Wishlist'
        verbose_name = 'wishlist'
        verbose_name_plural = 'wishlists'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username) + "'s_wishlist" 
        super(Wishlist, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('wishlist:all_items', kwargs={'wish_slug':self.slug})
    
    def __str__(self):
        return str(self.id)

class WishlistItem(models.Model):
    wishlist = models.ForeignKey(Wishlist, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'WishlistItem'