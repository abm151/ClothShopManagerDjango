from django.shortcuts import render
from inventory.models import Product


def dashboard_home(request):
    total_products = Product.objects.count()

    context = {
        "total_products": total_products,
    }

    return render(request, "dashboard/home.html", context)
