from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart_contents, name='cart'),
    path('add/<id>/', views.add_to_cart, name='add_to_cart'),
]
