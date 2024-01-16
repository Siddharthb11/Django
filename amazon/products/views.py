from django.shortcuts import render
from products.models import *
from products.forms import *

# Create your views here.
def display(request):
    result = Products_Table.objects.all()

    data = {'product_list':result}
    return render(request,'products/show.html',context=data)

def add(request):
    form = Product_Form()
    if request.method=="POST":
        form = Product_Form(request.POST)
        if(form.is_valid()):
            # instance = form.save()
            obj = Products_Table()
            obj.name = form.cleaned_data['name']
            obj.price = form.cleaned_data['price']
            obj.save()
            return display(request)
        
    data = {'prod_form':form}
    return render(request,'products/add.html',context=data)