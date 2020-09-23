from django.contrib import admin
from .models import Order, OrderItem
# Register your models here.


class OrderItemAdminInline(admin.TabularInline):
    model = OrderItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderItemAdminInline, )
    readonly_fields = ('order_number', 'date', 'order_total',
                       'grand_total', 'original_cart', 'stripe_pid')
    fields = ('order_number', 'profile', 'date', 'full_name',
              'email', 'phone_number',
              'postcode', 'street_address1',
              'street_address2', 'county',
              'order_total', 'grand_total', 'original_cart', 'stripe_pid')

    list_display = ('order_number', 'date', 'full_name',
                    'order_total', 'grand_total',)
    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
