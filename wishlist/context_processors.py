from .models import Wishlist, WishlistItem

def wishlist_counter(request):
    wishlist = Wishlist.objects.filter(user=request.user)
    return {'product_count': WishlistItem.objects.all().filter(wishlist=wishlist[:1]).count()}