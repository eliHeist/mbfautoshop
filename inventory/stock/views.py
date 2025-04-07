from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.utils import timezone
from django.views import View

from .models import StockTransaction, Part
from .forms import StockInForm

class StockTransactionListView(View):
    def get(self, request):
        transactions = StockTransaction.objects.all()
        return render(request, "stock/transaction_list.html", {"transactions": transactions})


class StockInCreateView(View):
    def get(self, request, pk):
        part = get_object_or_404(Part, id=pk)
        current_date = timezone.now().date().strftime("%d-%m-%Y")
        print(current_date)
        initial = {
            "part": part,
            "date": current_date
        }
        form = StockInForm(initial={"part": part})
        template_name = "stock/stock_in-create.html"
        context = {
            "form": form,
            "part": part
        }
        return render(request, template_name, context)
    
    def post(self, request, pk):
        part = get_object_or_404(Part, id=pk)
        form = StockInForm(request.POST)
        if form.is_valid():
            instance = form.save()
            return redirect(reverse_lazy("parts:detail", kwargs={"pk": pk}))
        
        template_name = "stock/stock_in-create.html"
        context = {
            "form": form,
            "part": part
        }
        return render(request, template_name, context)
