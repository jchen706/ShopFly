from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from . form import IdForm, OrderForm
from . requesting import getin, order2
from . order import Order
#import ../../../videoRecognition

def index(request):
    newform = IdForm()

    if request.method == 'POST':
        form = IdForm(request.POST)
        if form.is_valid():
            id = form.cleaned_data['the_id']
            try:
                price1 = getin(id)
                return render (request , 'new/index.html',{
                "price": price1,
                })
            except (KeyError):
                return render( request, 'new/index.html',{
                'error_message': "Item not found. Please try again!",
                })



    return render(request, 'new/index.html')



def ordering(request):
    form = OrderForm()

    if request.method == 'POST':
        print("Go")
        form = OrderForm(request.POST)
        if form.is_valid():
            try:
                productNum = form.cleaned_data['productNum']
                price1 = getin(productNum)
            except(KeyError):
                return render( request, 'new/order.html',{
                'error_message': "Item not found. Please try again!",
                })


            pickupLoc = form.cleaned_data['pickupLoc']
            customer_name = form.cleaned_data['customer_name']
            quantity = form.cleaned_data['quantity']



            order1 = Order(productNum, quantity, customer_name, pickupLoc, price1)
            order2(order1.payload())
            return render(request,'new/order.html',{
            'order_complete': "Order Complete", "price" : order1.getTotalPrice(),
            })

    return render(request, 'new/order.html')
