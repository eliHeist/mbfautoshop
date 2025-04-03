from django.urls import path

from . import views

app_name = "parts"

urlpatterns = [
    path("", views.PartListView.as_view(), name="list"),
    path("create/", views.PartCreateView.as_view(), name="create"),
    path("update/<int:part_id>/", views.PartUpdateView.as_view(), name="update"),
    path("delete/<int:part_id>/", views.PartDeleteView.as_view(), name="delete"),
    
    path("categories/", views.PartCategoryListView.as_view(), name="category-list"),
    path("categories/create/", views.PartCategoryCreateView.as_view(), name="category-create"),
    path("categories/update/<int:part_id>/", views.PartCategoryUpdateView.as_view(), name="category-update"),
    path("categories/delete/<int:part_id>/", views.PartCategoryDeleteView.as_view(), name="category-delete"),
]