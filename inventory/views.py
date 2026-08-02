from django.shortcuts import render, redirect
from .models import Product, Category, Brand


def product_list(request):
    products = Product.objects.all()

    return render(
        request,
        "inventory/product_list.html",
        {
            "products": products
        }
    )

def product_add(request):

    if request.method == "POST":

        sku = request.POST.get("sku")
        barcode = request.POST.get("barcode")
        name = request.POST.get("name")

        brand_name = request.POST.get("brand")
        category_name = request.POST.get("category")

        size = request.POST.get("size")
        color = request.POST.get("color")

        quantity = request.POST.get("quantity")
        purchase_price = request.POST.get("purchase_price")
        selling_price = request.POST.get("selling_price")


# Add these two lines here
        print("SKU:", sku)
        print("Barcode:", barcode)


        brand, created = Brand.objects.get_or_create(
            name=brand_name
        )

        category, created = Category.objects.get_or_create(
            name=category_name
        )
        

        Product.objects.create(
        sku=sku,
        barcode=barcode,
        name=name,
        brand=brand,
        category=category,
        size=size,
        color=color,
        purchase_price=purchase_price,
        selling_price=selling_price,
        quantity=quantity,
        )


        return redirect("product_list")


    return render(
        request,
        "inventory/product_add.html"
    )