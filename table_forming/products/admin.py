from django.contrib import admin

from .models import ProductsModel
# Register your models here.

@admin.register(ProductsModel)
class ProductsAdmin(admin.ModelAdmin):
    pass
