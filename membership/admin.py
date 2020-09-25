from django.contrib import admin
from .models import Membership, UserMembership, Subscription

# Register your models here.


class MembershipAdmin(admin.ModelAdmin):
    list_display = (
        'membership_type',
        'price',
        'duration_days',
    )


class UserMembershipAdmin(admin.ModelAdmin):
    list_display = (
        'member_profile',
        'user_membership',
    )


class SubscriptionAdmin(admin.ModelAdmin):
    list_display = (
        'subcription_membership',
        'membership_duration',
        'purchase_date',
        'expiration_date',
        'active',
        'cancelled',
    )


admin.site.register(Membership, MembershipAdmin)
admin.site.register(UserMembership, UserMembershipAdmin)
admin.site.register(Subscription, SubscriptionAdmin)
