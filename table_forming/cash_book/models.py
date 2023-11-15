from django.db import models


# Create your models here.
class CashBookModel(models.Model):
    product = models.ForeignKey(to="products.ProductsModel", related_name="cash_book", on_delete=models.CASCADE)
    price = models.DecimalField(decimal_places=2, max_digits=18)
    sale_date = models.DateTimeField()
