from django.urls import path

from . import views

app_name = "parts"

urlpatterns = [
    path("", views.PartListView.as_view(), name="list"),
    path("create/", views.PartCreateView.as_view(), name="create"),
    path("<int:part_id>/update/", views.PartDetailView.as_view(), name="detail"),
    path("<int:part_id>/update/", views.PartUpdateView.as_view(), name="update"),
    path("<int:part_id>/delete/", views.PartDeleteView.as_view(), name="delete"),
    
    path("categories/", views.PartCategoryListView.as_view(), name="category-list"),
    path("categories/create/", views.PartCategoryCreateView.as_view(), name="category-create"),
    path("categories/<int:part_id>/", views.PartCategoryDetailView.as_view(), name="category-detail"),
    path("categories/<int:part_id>/update/", views.PartCategoryUpdateView.as_view(), name="category-update"),
    path("categories/<int:part_id>/delete/", views.PartCategoryDeleteView.as_view(), name="category-delete"),
]