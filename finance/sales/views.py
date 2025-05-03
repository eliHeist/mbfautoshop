from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from finance.payments.forms import IncomeForm
from finance.payments.models import Income
from .models import Sale, SaleItem
from .forms import SaleModelForm, sale_item_formset

class SaleListView(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = "sales.view_sale"
    def get(self, request):
        sales = Sale.objects.all().order_by("-date")
        return render(request, "sales/sale-list.html", {"sales": sales})

class SaleCreateView(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = "sales.add_sale"
    def get(self, request):
        form = SaleModelForm()
        formset = sale_item_formset()
        payment_form = IncomeForm()
        
        context = {
            "form": form,
            "formset": formset,
            "payment_form": payment_form,
        }
        template_name = 'sales/sale-create.html'
        return render(request, template_name, context)

    def post(self, request):
        form = SaleModelForm(request.POST)
        if form.is_valid():
            print("\nSale valid")
            sale = form.save(commit=False)
            formset = sale_item_formset(request.POST, instance=sale)
            if formset.is_valid():
                print("\nFormset valid")
                sale.save()
                formset.save()
                
                payment_data = {
                    # "type": Payment.TYPES[0],
                    "sale": sale,
                    "payment_date": request.POST.get('payment_date', sale.date),
                    "amount": request.POST.get('amount'),
                    "method": request.POST.get('method'),
                }
                payment_form = IncomeForm(data=payment_data)
                if payment_form.is_valid():
                    print("\nPayment valid")
                    payment_form.save()
                    
                    return redirect("sales:list")
                else:
                    print("Invalid Payment details")
                    print(payment_form.errors)
            else:
                print("Invalid Formset details")
                print(formset.errors)
        else:
            print("Invalid Sale details")
            print(form.errors)
                
        payment_form = IncomeForm(request.POST)
        formset = sale_item_formset(request.POST)
        
        context = {
            "form": form,
            "formset": formset,
            "payment_form": payment_form,
        }
        template_name = 'sales/sale-create.html'
        return render(request, template_name, context)


