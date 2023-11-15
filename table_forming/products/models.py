from datetime import datetime
from uuid import uuid4

from django.db import models


class ProductsModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    price = models.DecimalField(decimal_places=2, max_digits=18)

    @property
    def orders_prev_month(self) -> int:
        return self.cash_book.filter(sale_date__month=datetime.now().month - 1).count()

    @property
    def orders_cur_month(self) -> int:
        return self.cash_book.filter(sale_date__month=datetime.now().month).count()
