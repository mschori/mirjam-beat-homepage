from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils.translation import gettext as _
from .models import Product


def wishlist(request):
    """
    View for Wishlist.
    List all wished items for the baby-time.
    :param request: request from user
    :return: rendered wishlist
    """
    wishlist_items = Product.objects.all().order_by('title')
    return render(request, 'baby_wishlist/wishlist.html', {'wishlist_items': wishlist_items})


def mark_product(request, product_id):
    """
    View for marking wishlist-product as purchased.
    :param request: request from user
    :param product_id: id of selected product
    :return: redirect to wishlist
    """
    try:
        product = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        messages.error(request, _('Product with this id does not exist!'))
        return redirect('baby_wishlist')
    product.purchased = True
    product.save()
    messages.success(request, _('Marked product as purchased!'))
    return redirect('baby_wishlist')


def unmark_product(request, product_id):
    """
    View for unmarking wishlist-product as purchased.
    :param request: request from user
    :param product_id: id of selected product
    :return: redirect to wishlist
    """
    try:
        product = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        messages.error(request, _('Product with this id does not exist!'))
        return redirect('baby_wishlist')
    product.purchased = False
    product.save()
    messages.success(request, _('Unmarked product as purchased!'))
    return redirect('baby_wishlist')
