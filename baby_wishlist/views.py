from django.shortcuts import render


def wishlist(request):
    return render(request, 'baby_wishlist/wishlist.html')
