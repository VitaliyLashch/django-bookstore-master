from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views
urlpatterns = [
    path('', views.main, name='main'),
    path('about_us', views.about_us, name='about-us'),
    path('account', views.account, name='account'),
    path('account-login', views.account_login, name='account-login'),
    path('account-register', views.account_register, name='account-register'),
    path('contact', views.contact, name='contact'),
    path('shop', views.search_page, name='shop'),
    path('shop_cart', views.shop_cart, name='shop_cart'),
    path('shop_compare', views.shop_compare, name='shop_compare'),
    path("shopping-cart/submit/", views.shopping_cart_submit, name="shopping_cart_submit"),
    path("shopping-cart/add/", views.shopping_cart_add, name="shopping_cart_add"),
    path("shopping-cart/remove/", views.shopping_cart_remove, name="shopping_cart_remove"),
    path('shop_threee_columns', views.search_page, name='shop_threee_columns'),
    path('shop_wishlist', views.shop_wishlist, name='shop_wishlist'),
    path('single_product/<int:id>', views.single_product, name='single_product'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('shop_checkout', views.shop_checkout, name='shop_checkout'),
    path('by', views.by, name='by'),
    path('logout', views.log, name='logout')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)