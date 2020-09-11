from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from .models import Order, OrderItem
from products.models import Product

from cart.contexts import cart_session

""" import stripe
 """
import json
# Create your views here.


def checkout(request):
    """renders checkout page"""

    cart = request.session.get('cart', {})
    if not cart:
        messages.error(
            request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout.html'
    context = {
        'order_form': order_form,
    }

    return render(request, template, context)
