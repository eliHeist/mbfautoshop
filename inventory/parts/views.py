from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Part, PartCategory
from .forms import PartCreateModelForm, PartCategoryModelForm

class PartListView(View):
    def get(self, request):
        parts = Part.objects.all()
        return render(request, "parts/part-list.html", {"parts": parts})

class PartDetailView(View):
    def get(self, request, pk):
        part = Part.objects.get(pk=pk)
        return render(request, "parts/part-detail.html", {"part": part})

class PartCreateView(View):
    def get(self, request):
        form = PartCreateModelForm()
        return render(request, "parts/part-create.html", {"form": form})

    def post(self, request):
        form = PartCreateModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("parts:list")
        return render(request, "parts/part-create.html", {"form": form})

class PartUpdateView(View):
    def get(self, request, part_id):
        part = get_object_or_404(Part, id=part_id)
        form = PartCreateModelForm(instance=part)
        return render(request, "parts/part-update.html", {"form": form})

    def post(self, request, part_id):
        part = get_object_or_404(Part, id=part_id)
        form = PartCreateModelForm(request.POST, instance=part)
        if form.is_valid():
            form.save()
            return redirect("parts:list")
        return render(request, "parts/part_form.html", {"form": form})

class PartDeleteView(View):
    def post(self, request, part_id):
        part = get_object_or_404(Part, id=part_id)
        part.delete()
        return redirect("parts:list")




class PartCategoryListView(View):
    def get(self, request):
        part_categories = PartCategory.objects.all()
        context = {
            "part_categories": part_categories,
        }
        template_name = "parts/category-list.html"
        return render(request, template_name, context)

class PartCategoryDetailView(View):
    def get(self, request, pk):
        part_category = PartCategory.objects.get(pk=pk)
        context = {
            "part_category": part_category,
        }
        template_name = "parts/category-detail.html"
        return render(request, template_name, context)

class PartCategoryCreateView(View):
    def get(self, request):
        form = PartCategoryModelForm()
        return render(request, "parts/category-create.html", {"form": form})

    def post(self, request):
        form = PartCategoryModelForm(request.POST)
        if form.is_valid():
            instance = form.save()
            return redirect("parts:list")
        return render(request, "parts/category-create.html", {"form": form})

class PartCategoryUpdateView(View):
    def get(self, request, part_id):
        part = get_object_or_404(PartCategory, id=part_id)
        form = PartCategoryModelForm(instance=part)
        return render(request, "parts/category-update.html", {"form": form})

    def post(self, request, part_id):
        part = get_object_or_404(PartCategory, id=part_id)
        form = PartCategoryModelForm(request.POST, instance=part)
        if form.is_valid():
            form.save()
            return redirect("parts:list")
        return render(request, "parts/category-update.html", {"form": form})

class PartCategoryDeleteView(View):
    def post(self, request, part_id):
        part = get_object_or_404(PartCategory, id=part_id)
        part.delete()
        return redirect("parts:category-list")