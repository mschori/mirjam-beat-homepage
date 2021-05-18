from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth import get_user
from django.utils.translation import gettext as _
from django.contrib.auth.decorators import login_required
from .forms import ContributeForm
from helpers import email_helper, babywishlist_helper
from .models import Product, Contribution
import os


def wishlist(request):
    """
    View for Wishlist.
    List all wished items for the baby-time.
    :param request: request from user
    :return: rendered wishlist
    """
    wishlist_items = Product.objects.all().order_by('purchased', '-price_progress')
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
    """
    View for contributing to a product.
    :param request: request from user
    :param product_id: id of selected product
    :return: rendered contribution-site
    """
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
            if form.cleaned_data['contribute'] > babywishlist_helper.calculate_remaining_price(product):
                messages.warning(request, _('You cant contribute more than the remaining price.'))
                return redirect('baby_wishlist')
            contribution = Contribution.objects.create(
                amount=form.cleaned_data['contribute'],
                comment=form.cleaned_data['comment'],
                product=product,
                user=user
            )
            babywishlist_helper.add_contribution_to_product(product, contribution)
            messages.success(request, _('Contribution confirmed.'))
            domain = get_current_site(request).domain
            email_helper.send_babywish_thank_you_mail(user, domain, contribution)
            return redirect('babywishlist_thank-you-page', contribution_id=contribution.id)
    return render(request, 'baby_wishlist/contribute.html', {'form': form, 'product': product})


@login_required()
def thank_you_page(request, contribution_id):
    """
    View for the thank-you-page after successfully contribution.
    :param request: request from user
    :param contribution_id: contribution-id
    :return: rendered thank-you-page
    """
    user = get_user(request)
    try:
        contribution = Contribution.objects.get(pk=contribution_id)
        if not contribution.user == user:
            messages.error(request, _('This contribution does not belong to you.'))
            return redirect('home')
    except Contribution.DoesNotExist:
        messages.error(request, _('No Contribution with this ID found.'))
        return redirect('home')
    bankname = os.environ.get('BANK_NAME')
    iban = os.environ.get('BANK_IBAN')
    to = os.environ.get('BANK_TO')
    return render(request, 'baby_wishlist/thanks_you.html',
                  {'contribution': contribution, 'bankname': bankname, 'iban': iban, 'to': to})


def delete_contribution(request, contribution_id):
    """
    View for deleting an existing contribution.
    :param request: request from user
    :param contribution_id: contribution-id
    :return: redirect to baby-wishlist
    """
    user = get_user(request)
    try:
        contribution = Contribution.objects.get(pk=contribution_id)
        if not contribution.user == user:
            messages.error(request, _('You can only delete your own contributions.'))
            return redirect('home')
    except Contribution.DoesNotExist:
        messages.error(request, _('No Contribution with this ID found.'))
        return redirect('home')
    babywishlist_helper.delete_contribution(contribution)
    messages.success(request, _('Successfully deleted your contribution.'))
    return redirect('baby_wishlist')
