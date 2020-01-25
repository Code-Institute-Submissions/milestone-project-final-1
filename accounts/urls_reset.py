from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from accounts import views


urlpatterns = [
	path('form/', auth_views.PasswordResetView.as_view(template_name='reset/password_reset_form.html'), name='password_reset_form'),

	path('done/', auth_views.PasswordResetDoneView.as_view(template_name='reset/password_reset_done.html'),
     name='password_reset_done'),

	path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='reset/password_reset_confirm.html'), name='password_reset_confirm'),

	path('password-reset-confirm/done/', auth_views.PasswordResetCompleteView.as_view(template_name='reset/password_reset_complete.html'),
     name='password_reset_complete'),
]

