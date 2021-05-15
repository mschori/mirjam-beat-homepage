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


register.filter(calculate_progress)
