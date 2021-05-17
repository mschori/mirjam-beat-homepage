from django.urls import path
from . import views

urlpatterns = [
    path('', views.wishlist, name='baby_wishlist'),
    path('mark/<int:product_id>', views.mark_product, name='mark_product'),
    path('unmark/<int:product_id>', views.unmark_product, name='unmark_product'),
    path('contribute/<int:product_id>', views.contribute_to_product, name='contribute_to_product'),
    path('thank-you/<int:contribution_id>', views.thank_you_page, name='babywishlist_thank-you-page'),
    path('contribute/<int:contribution_id>/delete', views.delete_contribution, name='delete_contribution'),
]
