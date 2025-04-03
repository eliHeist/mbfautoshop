from django.urls import path

from . import views

app_name = "stock"

urlpatterns = [
    path("", views.StockTransactionListView.as_view(), name="list"),
    path("add/", views.StockTransactionCreateView.as_view(), name="add"),
]