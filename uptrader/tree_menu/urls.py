from django.urls import path

from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('main/', views.main_menu, name='main_menu'),
    path('secondary/', views.secondary_menu, name='secondary_menu'),
    path('main/products/', views.products, name='products_list'),
    path('main/products/phones/', views.phones, name='phones_list'),
    path('main/products/laptops/', views.laptops, name='laptops_list'),
    path('secondary/info/', views.info, name='info_page'),
    path('secondary/info/contacts/', views.contacts, name='contacts_page'),
    path('secondary/info/faq/', views.faq, name='faq_page'),
    path('secondary/about/', views.about, name='about_page'),
]