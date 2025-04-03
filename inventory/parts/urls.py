from django.urls import path

from . import views

app_name = "parts"

urlpatterns = [
    path("", views.PartListView.as_view(), name="list"),
    path("add/", views.PartCreateView.as_view(), name="create"),
    path("edit/<int:part_id>/", views.PartUpdateView.as_view(), name="update"),
    path("delete/<int:part_id>/", views.PartDeleteView.as_view(), name="delete"),
]