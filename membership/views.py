from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.db.models import Q
from django.db.models.functions import Lower

from membership.models import Membership, UserMembership, Subscription


# Create your views here.


def all_membership(request):
    """ renders all membership"""

    membership = Membership.objects.all()
    monthly = membership[0]
    annually = membership[1]
    context = {
        'monthly': monthly,
        'annually': annually,
    }

    return render(request, 'membership.html', context)
