from baby_wishlist.models import Product, Contribution


def is_product_price_progress_finished(product: Product):
    """
    Check if price-progress is greater or equal the full-price of a product.
    :param product: product-object
    :return: boolean
    """
    return product.price_progress >= product.price_full


def is_progress_price_null(product: Product):
    """
    Check if the progress-price of a product is Null.
    :param product: product to check
    :return: boolean
    """
    return product.price_progress <= 0


def calculate_progress(product: Product):
    """
    Calculate current progress of product-purchase.
    :param product: product-object
    :return: calculated progress
    """
    return int(product.price_progress / product.price_full * 100)


def calculate_remaining_price(product: Product):
    """
    Calculate the remaining price of a product based on current progress.
    :param product: product-object
    :return: calculated remaining price
    """
    remaining_price = product.price_full - product.price_progress
    return int(remaining_price) if remaining_price >= 0 else 0


def add_contribution_to_product(product: Product, contribution: Contribution):
    """
    Add a contribution to a product.
    Simply add the contribution-amount to the progress-price.
    :param product: product-object
    :param contribution: contribution-object
    """
    product.price_progress = product.price_progress + contribution.amount
    if is_product_price_progress_finished(product):
        product.purchased = True
    product.save()


def delete_contribution(contribution: Contribution):
    """
    Delete an existing contribution.
    First remove contribution-amount from products price-progress.
    :param contribution: contribution-object
    """
    product = contribution.product
    product.price_progress = product.price_progress - contribution.amount
    if not is_product_price_progress_finished(product):
        product.purchased = False
    product.save()
    contribution.delete()
