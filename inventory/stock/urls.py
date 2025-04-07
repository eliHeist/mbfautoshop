from django.urls import path

from . import views

app_name = "stock"

urlpatterns = [
    path("", views.StockTransactionListView.as_view(), name="list"),
    path("restock/<int:pk>/", views.StockInCreateView.as_view(), name="restock"),
]