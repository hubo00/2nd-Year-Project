from django.db import models
from django.urls import reverse
from accounts.models import CustomUser
from shop.models import Product
from django.utils.text import slugify

# Class for Wishlist model which is connected to WishlistItem via a one-many relationship
class Wishlist(models.Model):
    # User field acts as a foreign key to link the wishlist to the user
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=120, unique=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Wishlist'
        verbose_name = 'wishlist'
        verbose_name_plural = 'wishlists'

    # Function to save the slug as a concatenation of the user's username and a string
    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username) + "'s_wishlist" 
        super(Wishlist, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('wishlist:all_items', kwargs={'wish_slug':self.slug})
    
    def __str__(self):
        return str(self.id)

# Class for Wishlist items which are stored as a many-one relationship with the Wishlist    
class WishlistItem(models.Model):
    # Wishlist field acts as a foreign key to link this item to the wishlist
    wishlist = models.ForeignKey(Wishlist, on_delete=models.CASCADE)
    # Product field acts as a foreign key to link this item with a product from the store
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'WishlistItem'