from django.contrib import admin

from .models import CashBookModel

# Register your models here.


@admin.register(CashBookModel)
class CashBookAdmin(admin.ModelAdmin):
    fields = ["product", "price", "sale_date"]
