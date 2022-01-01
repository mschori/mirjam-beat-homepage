from django import template
from wishlist.models import Product
from helpers import wishlist_helper

register = template.Library()


def calculate_progress(product: Product):
    """
    Template-Tag.
    Calculate current progress of product-purchase.
    :param product: product-object
    :return: calculated progress
    """
    return babywishlist_helper.calculate_progress(product)


def is_progress_price_null(product: Product):
    """
    Template-Tag.
    Check if progress-price is zero.
    :param product: product to check
    :return: boolean
    """
    return babywishlist_helper.is_progress_price_null(product)


def calculate_remaining_price(product: Product):
    """
    Template-Tag.
    Calculate the remaining price of a product based on current progress.
    :param product: product-object
    :return: calculated remaining price
    """
    return babywishlist_helper.calculate_remaining_price(product)


def get_half_remaining_price(product: Product):
    """
    Template-Tag.
    Calculate remaining price and return half of it.
    :param product: product-object
    :return: half of remaining price
    """
    return babywishlist_helper.calculate_remaining_price(product) / 2


register.filter(calculate_progress)
register.filter(is_progress_price_null)
register.filter(calculate_remaining_price)
register.filter(get_half_remaining_price)
