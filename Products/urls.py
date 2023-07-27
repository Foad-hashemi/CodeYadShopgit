from django.urls import path
from . import views

app_name = 'Product'

urlpatterns = [
    path('<int:pk>', views.ProductDetail.as_view(), name='detail')
]