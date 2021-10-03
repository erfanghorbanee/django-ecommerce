from django.urls import path
from .views import basket_view, add_to_basket, delete_from_basket, checkout

urlpatterns = [
    path('basket/', basket_view, name='basket'),
    path('add-to-basket/', add_to_basket, name='add_to_basket'),
    path('delete-from-basket/<int:product_id>/', delete_from_basket, name='delete_from_basket'),
    path('checkout/', checkout, name='checkout'),

]