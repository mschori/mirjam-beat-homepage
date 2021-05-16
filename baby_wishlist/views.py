from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import get_user
from django.utils.translation import gettext as _
from django.contrib.auth.decorators import login_required
from .forms import ContributeForm
from .models import Product, Contribution


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


@login_required()
def contribute_to_product(request, product_id):
    user = get_user(request)
    form = ContributeForm()
    try:
        product = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        messages.error(request, _('Product with this id does not exist!'))
        return redirect('baby_wishlist')
    if request.method == 'POST':
        form = ContributeForm(request.POST)
        if form.is_valid():
            Contribution.objects.create(
                amount=form.cleaned_data['contribute'],
                comment=form.cleaned_data['comment'],
                product=product,
                user=user
            )
            messages.success(request, _('Contribution confirmed.'))
            # TODO Email senden
            # TODO Bestätigungs-Seite
    return render(request, 'baby_wishlist/contribute.html', {'form': form, 'product': product})
