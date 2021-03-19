from django.shortcuts import redirect, render
from .models import Order, Product

def index(request):
    if not "total" in request.session:
        request.session['total'] = 0
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "store/index.html", context)

def checkout(request):
    context = Product.objects.get(id = request.POST["id"])
    quantity_from_form = int(request.POST["quantity"])
    price_from_form = float(context.price)
    total_charge = round(quantity_from_form * price_from_form, 2)
    print("Charging credit card...")
    Order.objects.create(quantity_ordered=quantity_from_form, total_price=total_charge)
    request.session['total'] += round(total_charge,2)
    return redirect("/thanks/")
    
def thanks(request):
    pass
    context = { "current_order" : Order.objects.last()   
     }
    return render (request, "store/checkout.html", context)