from django.urls import path
from . import views

urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('confirm-mail/<uidb64>/<token>', views.confirm_email, name='confirm_email'),
    path('confirm-mail/resend', views.resend_confirm_email, name='confirm_email_resend'),
]
