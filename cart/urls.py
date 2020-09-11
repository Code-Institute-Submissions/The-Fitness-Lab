from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart_contents, name='cart'),
    path('add/<id>/', views.add_to_cart, name='add_to_cart'),
    path('adjust/<item_id>/', views.adjust_cart, name='adjust_cart'),
    path('remove/<item_id>/', views.cart_remove, name='cart_remove')
]
