from django.urls import path

from . import views

app_name = "parts"

urlpatterns = [
    path("", views.PartListView.as_view(), name="list"),
    path("create/", views.PartCreateView.as_view(), name="create"),
    path("<int:pk>/", views.PartDetailView.as_view(), name="detail"),
    path("<int:pk>/update/", views.PartUpdateView.as_view(), name="update"),
    path("<int:pk>/delete/", views.PartDeleteView.as_view(), name="delete"),
    
    path("categories/", views.PartCategoryListView.as_view(), name="category-list"),
    path("categories/create/", views.PartCategoryCreateView.as_view(), name="category-create"),
    path("categories/<int:pk>/", views.PartCategoryDetailView.as_view(), name="category-detail"),
    path("categories/<int:pk>/update/", views.PartCategoryUpdateView.as_view(), name="category-update"),
    path("categories/<int:pk>/delete/", views.PartCategoryDeleteView.as_view(), name="category-delete"),
]