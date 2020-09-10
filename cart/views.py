from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from products.models import Product


# Create your views here.


def cart_contents(request):
    """
    View that renders the cart content page
    """
    return render(request, "cart.html")


def add_to_cart(request, id):
    """
    Add a quantity of the specified product to the shopping bag
    """
    product = get_object_or_404(Product, pk=id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})
    if id in cart:
        cart[id] = int(cart[id]) + quantity
        messages.success(
            request, f'Updated {product.name} quantity to {cart[id]}')
    else:
        cart[id] = cart.get(id, quantity)
        messages.success(request, f'Added {product.name} to your bag')

    request.session['cart'] = cart
    print(request.session['cart'])
    return redirect(redirect_url)
