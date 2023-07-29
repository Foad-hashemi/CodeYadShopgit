from django.contrib import admin
from .models import *


class InfoStack(admin.StackedInline):
    model = Information

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title','price')
    inlines = (InfoStack,)

# Register your models here.

admin.site.register(Information)
admin.site.register(Size)
admin.site.register(Color)
