from django.urls import path
from . import views
from django.contrib.auth.views import (
    PasswordResetView, 
    PasswordResetDoneView, 
    PasswordResetConfirmView,
    PasswordResetCompleteView
)

urlpatterns = [
     path('', views.home, name='home'),
     path('register', views.register, name='register'),
     path('signin', views.signin, name='signin'),
     path('signout', views.signout, name='signout'),
     path('password-reset/', 
         PasswordResetView.as_view(template_name='account/password_reset.html'),name='password-reset'),
    path('password-reset/done/',
          PasswordResetDoneView.as_view(template_name='account/password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
          PasswordResetConfirmView.as_view(template_name='account/password_reset_confirm.html'),name='password_reset_confirm'),
    path('password-reset-complete/',
          PasswordResetCompleteView.as_view(template_name='account/password_reset_complete.html'),name='password_reset_complete'),
]
