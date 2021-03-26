from .models import Wishlist, WishlistItem
from django.contrib.auth.decorators import login_required

def wishlist_counter(request):
    if request.user.id:
        wishlist = Wishlist.objects.filter(user=request.user)
        return {'product_count': WishlistItem.objects.all().filter(wishlist=wishlist[:1]).count()}
    return {}