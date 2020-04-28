from django.urls import path
from payu_app import views

urlpatterns = [
    path('checkout/', views.checkout, name='order.checkout'),
    path('success/', views.success, name='order.success'),
    path('failure/', views.failure, name='order.failure'),
    path('cancel/', views.cancel, name='order.cancel'),
]