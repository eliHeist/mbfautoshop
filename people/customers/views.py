from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Customer
from .forms import CustomerForm

class CustomerListView(View):
    def get(self, request):
        customers = Customer.objects.all()
        return render(request, "customers/customer_list.html", {"customers": customers})

class CustomerCreateView(View):
    def get(self, request):
        form = CustomerForm()
        return render(request, "customers/customer_form.html", {"form": form})

    def post(self, request):
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("customers:list")
        return render(request, "customers/customer_form.html", {"form": form})

class CustomerDeleteView(View):
    def post(self, request, customer_id):
        customer = get_object_or_404(Customer, id=customer_id)
        customer.delete()
        return redirect("customers:list")
