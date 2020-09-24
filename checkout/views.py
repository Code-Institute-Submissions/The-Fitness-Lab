from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from decimal import Decimal

from .forms import OrderForm
from .models import Order, OrderItem
from products.models import Product
from accounts.models import UserAccount
from accounts.forms import ProfileForm
from cart.contexts import cart_session
from django.db.models import Count

import stripe
import json


def thanks(request, order_number):
    """
    Renders successfull payments in checkout
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)

    if request.user.is_authenticated:
        profile = UserAccount.objects.get(user=request.user)
        order.profile = profile
        order.save()

        # Save the user's info
        if save_info:
            profile_data = {
                'name': order.full_name,
                'email': order.email,
                'phone_number': order.phone_number,
                'street_address1': order.street_address1,
                'street_address2': order.street_address2,
                'county': order.county,
                'postcode': order.postcode,
            }
            profile_form = ProfileForm(profile_data, instance=profile)
            if profile_form.is_valid():
                profile_form.save()

    # Shows the grand total of purchase in mail
    items = order.lineitems.all()
    grand_total = Decimal(0)
    for item in items:

        item_total = Decimal(item.product.price * item.quantity)
        grand_total += item_total
        print(grand_total)

    # Sends confirmation email to the customer
    cust_email = order.email
    subject = render_to_string(
        'confirmation_email_subject.txt',
        {'order': order})
    body = render_to_string(
        'confirmation_email.txt',
        {'order': order, 'grand_total': grand_total, 'contact_email': settings.DEFAULT_FROM_EMAIL})

    send_mail(
        subject,
        body,
        settings.DEFAULT_FROM_EMAIL,
        [cust_email]
    )
    messages.success(request, f'Payment Succesful!')

    if 'cart' in request.session:
        del request.session['cart']

    template = 'thanks.html'
    context = {
        'order': order,
        'grand_total': grand_total,
    }

    return render(request, template, context)


@login_required
def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        cart = request.session.get('cart', {})
        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'postcode': request.POST['postcode'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
        }
        profile_order_form = OrderForm(form_data)
        if profile_order_form.is_valid():
            order = profile_order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_cart = json.dumps(cart)
            order.save()
            for item_id, quantity in cart.items():
                product = Product.objects.get(id=item_id)
                if isinstance(quantity, int):
                    order_line_item = OrderItem(
                        order=order,
                        product=product,
                        quantity=quantity,
                    )
                    order_line_item.save()

            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('thanks', args=[order.order_number]))
        else:
            messages.error(
                request, 'Unable to process your payment, Please check your information')
    else:
        cart = request.session.get('cart', {})
        if not cart:
            messages.error(
                request, "The cart is empty")
            return redirect(reverse('products'))

        current_cart = cart_session(request)
        total = current_cart['total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        # Autofill the billing info from the user profile
        if request.user.is_authenticated:
            try:
                profile = UserAccount.objects.get(user=request.user)
                profile_order_form = OrderForm(initial={
                    'full_name': profile.name,
                    'email': profile.email,
                    'phone_number': profile.phone_number,
                    'street_address1': profile.street_address1,
                    'street_address2': profile.street_address2,
                    'county': profile.county,
                    'postcode': profile.postcode,
                })
            except UserAccount.DoesNotExist:
                profile_order_form = OrderForm()
        else:
            profile_order_form = OrderForm()

    template = 'checkout.html'
    context = {
        'profile_order_form': profile_order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)
