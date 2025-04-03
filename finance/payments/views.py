from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Payment
from .forms import PaymentForm

class PaymentListView(View):
    def get(self, request):
        payments = Payment.objects.all()
        return render(request, "payments/payment_list.html", {"payments": payments})

class PaymentCreateView(View):
    def get(self, request):
        form = PaymentForm()
        return render(request, "payments/payment_form.html", {"form": form})

    def post(self, request):
        form = PaymentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("payments:list")
        return render(request, "payments/payment_form.html", {"form": form})
