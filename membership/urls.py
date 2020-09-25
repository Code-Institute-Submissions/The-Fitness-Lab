from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_membership, name='all_membership'),
    #path('<int:product_id>/', views.product_detail, name='product_detail'),
]
