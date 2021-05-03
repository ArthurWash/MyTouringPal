from django.urls import path

from . import views

urlpatterns = [
    path('thank_you', views.thank_you, name='thank_you'),
    path('welcome', views.welcome, name='welcome'),
    path('book_a_show', views.book, name='Book_a_show'),
    path('ajax-demo', views.ajax_demo, name='ajax-demo'),
    path('auth', views.auth, name='auth'),
    path('venues', views.venues, name='venues'),
]