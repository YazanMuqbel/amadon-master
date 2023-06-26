from django.shortcuts import render, redirect
from .models import Order, Product

def index(request):
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "store/index.html", context)

def checkout(request):
    if request.method== "POST":
        quantity_from_form = int(request.POST["quantity"])
        price_from_form = float(request.POST["price"])
        total_charge = quantity_from_form * price_from_form
        print("Charging credit card...")
        Order.objects.create(quantity_ordered=quantity_from_form, total_price=total_charge)
        context = {'total_charge': total_charge, 'total_qty' : quantity_from_form}
    
    return redirect('thank_you')

#*************************************************8
def checkout(request):
    if request.method == 'POST':
        order = Order()
        order.quantity_ordered = request.POST['quantity']
        order.total_price = request.POST['price']
        order.save()
    return redirect('thank_you', id=order.id)


"""def thank_you(request):
    order = Order.objects.get()
    context = {
        'order': order
    }
    return render(request, "checkout.html", context)"""


def thank_you(request, id):   
    order = Order.objects.get(id=id)
    context = {
        'id': id,
    }
    return render(request, "checkout.html", context)