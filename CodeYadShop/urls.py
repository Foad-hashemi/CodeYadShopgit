from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from . import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Home.urls')),
    path('', include('Accounts.urls')),
    path('product/', include('Products.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

