from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.shortcuts import render
from products.models import ProductsModel

# Create your views here.


@login_required
def report(request: HttpRequest):
    context = {"products": ProductsModel.objects.all()}

    return render(request=request, template_name="report_template.html", context=context)
