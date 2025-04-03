from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Supplier
from .forms import SupplierForm

class SupplierListView(View):
    def get(self, request):
        suppliers = Supplier.objects.all()
        return render(request, "suppliers/supplier_list.html", {"suppliers": suppliers})

class SupplierCreateView(View):
    def get(self, request):
        form = SupplierForm()
        return render(request, "suppliers/supplier_form.html", {"form": form})

    def post(self, request):
        form = SupplierForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("suppliers:list")
        return render(request, "suppliers/supplier_form.html", {"form": form})
