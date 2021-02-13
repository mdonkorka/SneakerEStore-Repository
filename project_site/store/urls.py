from django.urls import path, include

from . import views
urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('store/', views.store, name="store"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('about/', views.about, name="about" ),

    path('update_item/', views.updateItem, name="update_item"),

    path('process_order/', views.processOrder, name="process_order"),
]
