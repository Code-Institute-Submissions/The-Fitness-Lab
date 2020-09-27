from django.urls import path
from . import views
""" 
from .webhooks import webhook
 """
urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('membership/<int:membership_id>/', views.membership_checkout,
         name='membership_checkout'),
    path('thanks/<order_number>', views.thanks, name='thanks'),
    path('membership/payment/<int:membership_id>',
         views.membership_success,
         name='membership_success'),

]
