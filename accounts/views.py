from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from decimal import Decimal
from .models import UserAccount
from .forms import ProfileForm

from checkout.models import Order


@login_required
def account_profile(request):
    """ Renders the user's profile """

    profile = get_object_or_404(UserAccount, user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request,
                           ('Update failed. Please ensure '
                            'the form is valid.'))
    else:
        form = ProfileForm(instance=profile)

    orders = profile.orders.all()
    # show 5 products per page
    paginator = Paginator(orders, 5)
    page = request.GET.get('page')
    if orders:
        try:
            orders = paginator.page(page)
        except PageNotAnInteger:
            orders = paginator.page(1)
        except EmptyPage:
            orders = paginator.page(paginator.num_pages)

    # Show total of the product
    for order in orders:
        for item in order.lineitems.all():
            grand_total = Decimal(0)
            item_total = Decimal(0)
            item_total += item.product.price * item.quantity
            grand_total += int(item_total + item_total)

    template = 'user-profile.html'
    context = {
        'form': form,
        'orders': orders,
        'profile': profile,
        # 'grand_total': grand_total,
        'only_profile': True,

    }

    return render(request, template, context)
