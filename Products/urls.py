from django.urls import path
from . import views

app_name = 'Product'

urlpatterns = [
    path('list', views.ProductList.as_view(), name='list'),
    path('<int:pk>', views.ProductDetail.as_view(), name='detail')
]