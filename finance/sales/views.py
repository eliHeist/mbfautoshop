from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Sale, SaleItem
from .forms import SaleModelForm

class SaleListView(View):
    def get(self, request):
        sales = Sale.objects.all()
        return render(request, "sales/sale_list.html", {"sales": sales})

class SaleCreateView(View):
    def get(self, request):
        form = SaleModelForm()
        return render(request, "sales/sale_form.html", {"form": form})

    def post(self, request):
        form = SaleModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("sales:list")
        return render(request, "sales/sale_form.html", {"form": form})
