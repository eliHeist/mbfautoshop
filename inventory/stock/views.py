from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import StockTransaction, Part
from .forms import StockTransactionForm

class StockTransactionListView(View):
    def get(self, request):
        transactions = StockTransaction.objects.all()
        return render(request, "stock/transaction_list.html", {"transactions": transactions})

class StockTransactionCreateView(View):
    def get(self, request):
        form = StockTransactionForm()
        return render(request, "stock/transaction_form.html", {"form": form})

    def post(self, request):
        form = StockTransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save()
            part = transaction.part
            if transaction.transaction_type == "IN":
                part.stock_quantity += transaction.quantity
            elif transaction.transaction_type == "OUT":
                part.stock_quantity -= transaction.quantity
            part.save()
            return redirect("transactions:list")
        return render(request, "stock/transaction_form.html", {"form": form})
