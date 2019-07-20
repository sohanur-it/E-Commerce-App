from django.contrib import admin

# Register your models here.
from .models import Post, Item, OrderItem, Order, Address, UserProfile, Payment, Coupon, Refund


def make_refund_accepted(modeladmin, request, queryset):
  queryset.update(refund_requested=False, refund_granted=True)


make_refund_accepted.short_description = 'Update order to refund granted '


class OrderAdmin(admin.ModelAdmin):
  list_display = ['user',
                  'ordered',
                  'being_received',
                  'received',
                  'refund_requested',
                  'refund_granted',
                  'billing_address',
                  'shipping_address',
                  'payment',
                  'coupon']

  list_display_links = ['user',
                        'billing_address',
                        'shipping_address',
                        'payment', 'coupon']

  list_filter = ['ordered',
                 'being_received',
                 'received',
                 'refund_requested',
                 'refund_granted']

  search_fields = ['user__username',
                   'ref_code']

  actions = [make_refund_accepted]


class AddressAdmin(admin.ModelAdmin):
  list_display = [
      'user',
      'street_address',
      'apartment_address',
      'country',
      'zip',
      'address_type',
      'default'
  ]
  list_filter = ['default', 'address_type', 'country']
  search_fields = ['user', 'street_address', 'apartment_address', 'zip']


admin.site.register(Post)
admin.site.register(Item)
admin.site.register(OrderItem)
admin.site.register(Order, OrderAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(UserProfile)
admin.site.register(Payment)
admin.site.register(Coupon)
