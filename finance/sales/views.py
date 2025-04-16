from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Sale, SaleItem
from .forms import SaleModelForm, sale_item_formset

class SaleListView(View):
    def get(self, request):
        sales = Sale.objects.all()
        return render(request, "sales/sale-list.html", {"sales": sales})

class SaleCreateView(View):
    def get(self, request):
        form = SaleModelForm()
        formset = sale_item_formset()
        
        context = {
            "form": form,
            "formset": formset,
        }
        template_name = 'sales/sale-create.html'
        return render(request, template_name, context)

    def post(self, request):
        form = SaleModelForm(request.POST)
        formset = sale_item_formset(request.POST)
        if form.is_valid() and formset.is_valid():
            form.save()
            return redirect("sales:list")
        context = {
            "form": form,
            "formset": formset,
        }
        template_name = 'sales/sale-create.html'
        return render(request, template_name, context)
