from django.shortcuts import render
from django.http import HttpRequest
from django.contrib.auth.decorators import login_required

from products.models import ProductsModel
# Create your views here.

@login_required
def report(request: HttpRequest):
    context = {
        "products": ProductsModel.objects.all()
    }

    return render(request=request, template_name="report_template.html", context=context)