from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ('email', 'is_active', 'is_staff', 'is_superuser', 'firstname', 'lastname', 'email_confirmed')
    list_filter = ('is_active', 'is_staff', 'is_superuser', 'email_confirmed')
    fieldsets = (
        (None, {'fields': ('email', 'firstname', 'lastname', 'password', 'email_confirmed')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_active')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(User, CustomUserAdmin)
