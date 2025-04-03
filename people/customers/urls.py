from django.urls import path

from . import views

app_name = "customers"

urlpatterns = [
    path("", views.CustomerListView.as_view(), name="list"),
    path("add/", views.CustomerCreateView.as_view(), name="add"),
    # path("edit/<int:customer_id>/", views.CustomerUpdateView.as_view(), name="edit"),
    path("delete/<int:customer_id>/", views.CustomerDeleteView.as_view(), name="delete"),
]