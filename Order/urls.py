from django.urls import path
from . import views

app_name = 'Order'

urlpatterns = [
    path('detail', views.CartView.as_view(), name='cart'),
    path('add/<int:pk>', views.CartHandelView.as_view(), name='cartadd'),
    path('delete/<str:upk>', views.CartDeleteItem.as_view(), name='cartitmedel')
]