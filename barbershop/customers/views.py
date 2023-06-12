from django.shortcuts import render, redirect, get_object_or_404
from .models import Customers
from .forms import CustomerForm
# Create your views here.

def customer_list(request):

    customers = Customers.objects.all()
    print(customers)
    return render(request, 'Customer.html', {'customers':customers})

def customer_new(request):
    
    form = CustomerForm(request.POST, None)

    if form.is_valid():
        form.save()
        return redirect('customer_list')

    return render(request, 'Customer_form.html', {'form':form})

def customer_update(request, id):

    customer = get_object_or_404(Customers, pk=id)
    form = CustomerForm(request.POST or None, instance=customer)

    if form.is_valid():
        form.save()
        return redirect('customer_list')

    return render(request, 'Customer_form.html', {'form':form})

def customer_delete(request, id):
    customer = get_object_or_404(Customers, pk=id)
    form = form = CustomerForm(request.POST or None, instance=customer)

    if request.method == "POST":
        customer.delete()
        return redirect('customer_list')
    
    return render(request, 'Customer_form_delete.html', {'form':form})