from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.utils import timezone
from django.views import View

from .models import StockTransaction, Part
from .forms import StockInTransactionFormSet, StockInForm

from finance.purchases.forms import PurchaseForm
from finance.purchases.models import Purchase

class StockTransactionListView(View):
    def get(self, request):
        transactions = StockTransaction.objects.all()
        return render(request, "stock/transaction_list.html", {"transactions": transactions})


class StockInCreateView(View):
    def get(self, request, pk):
        part = Part.objects.get(pk=pk)
        current_date = timezone.now().date().strftime("%d-%m-%Y")
        stock_initial = {
            "part": part,
        }
        stock_form = StockInForm(initial=stock_initial)
        
        
        purchase_initial = {
            "type": Purchase.TYPES[1],
        }
        purchase_form = PurchaseForm(initial=purchase_initial)
        template_name = "stock/stock_in-create.html"
        context = {
            "stock_form": stock_form,
            "purchase_form": purchase_form,
            "part": part,
        }
        return render(request, template_name, context)
    
    def post(self, request, pk):
        part = get_object_or_404(Part, id=pk)
        stock_form = StockInForm(request.POST)
        purchase_form = PurchaseForm(request.POST)
        if stock_form.is_valid() and purchase_form.is_valid():
            stock = stock_form.save()
                
            purchase = purchase_form.save()
            purchase.re_stocks.set([stock])
            
            break_even = purchase.amount / stock.quantity
            
            if break_even > (part.break_even_price or 0):
                part.break_even_price = break_even
                part.save()
            
            return redirect(reverse_lazy("parts:detail", kwargs={"pk": pk}))
        
        template_name = "stock/stock_in-create.html"
        context = {
            "stock_form": stock_form,
            "purchase_form": purchase_form,
            "part": part,
        }
        return render(request, template_name, context)
