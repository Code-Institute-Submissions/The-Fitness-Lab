from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserAccount
from .forms import ProfileForm

from checkout.models import Order


def account_profile(request):
    """ Display the user's profile. """
    #user = User.objects.get(email=request.user.email)
    #username = User.objects.get(username=request.user.username)
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
    template = 'user-profile.html'
    context = {
        'form': form,
        'orders': orders,
        'profile': profile,
        # 'user': user,
        # 'username': username,
        'on_profile_page': True
    }

    return render(request, template, context)
