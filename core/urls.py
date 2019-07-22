from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from .views import HomeView,\
    ItemDetailView,\
    CheckoutView,\
    add_to_cart,\
    remove_from_cart,\
    OrderSummaryView,\
    remove_single_item_from_cart,\
    PaymentMethod,\
    AddCouponView,\
    CategoryListView,\
    RequestRefundView,\
    ProfileView,\
    product
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('category/<category>', CategoryListView.as_view(), name='category-list'),
    path('product/<slug:slug>', ItemDetailView.as_view(), name='product-detail'),
    path('add-to-cart/<slug:slug>', add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<slug:slug>', remove_from_cart, name='remove-from-cart'),
    path('remove-single-item-from-cart/<slug:slug>', remove_single_item_from_cart, name='remove-single-item-from-cart'),
    path('checkout/', CheckoutView.as_view(), name='check-out'),
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    path('payment/<payment_option>', PaymentMethod.as_view(), name='payment'),
    path('payment/<payment_option>', PaymentMethod.as_view(), name='payment'),
    path('add-coupon/', AddCouponView.as_view(), name='add-coupon'),
    path('request-refund/<str:ref_code>', RequestRefundView.as_view(), name='request-refund'),
    path('profile/', ProfileView.as_view(), name='profile'),

]

# for adding media file settings
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
