from django.shortcuts import render
from inventory.models import Product, Brand, Category


def dashboard_home(request):

    total_products = Product.objects.count()

    total_brands = Brand.objects.count()

    total_categories = Category.objects.count()

    total_stock = sum(
        Product.objects.values_list("quantity", flat=True)
    )

    low_stock_products = Product.objects.filter(
        quantity__lte=5
    )

    context = {
        "total_products": total_products,
        "total_brands": total_brands,
        "total_categories": total_categories,
        "total_stock": total_stock,
        "low_stock_products": low_stock_products,
    }

    return render(
        request,
        "dashboard/home.html",
        context
    )
