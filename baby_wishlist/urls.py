from django.urls import path
from . import views

urlpatterns = [
    path('', views.wishlist, name='baby_wishlist'),
    path('mark/<int:product_id>', views.mark_product, name='mark_product'),
    path('unmark/<int:product_id>', views.unmark_product, name='unmark_product'),
]
