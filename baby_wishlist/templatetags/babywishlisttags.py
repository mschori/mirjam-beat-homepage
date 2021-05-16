from django import template
from baby_wishlist.models import Product

register = template.Library()


def calculate_progress(product: Product):
    """
    Calculate current progress of product-purchase.
    :param product: product-object
    :return: calculated progress
    """
    return product.price_progress / product.price_full * 100


def calculate_remaining_price(product: Product):
    """
    Calculate the remaining price of a product based on current progress.
    :param product: product-object
    :return: calculated remaining price
    """
    remaining_price = product.price_full - product.price_progress
    return remaining_price if remaining_price >= 0 else 0


register.filter(calculate_progress)
register.filter(calculate_remaining_price)
