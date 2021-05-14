from django.contrib import admin
from .models import User


@admin.register(User)
class BabyWishlistAdmin(admin.ModelAdmin):
    """
    Admin-Registration for Users.
    """
    pass
