from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Part
from .forms import PartCreateModelForm, PartTypeModelForm

class PartListView(View):
    def get(self, request):
        parts = Part.objects.all()
        return render(request, "parts/part-list.html", {"parts": parts})

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
        form = PartCreateModelForm, PartTypeModelForm(instance=part)
        return render(request, "parts/part-update.html", {"form": form})

    def post(self, request, part_id):
        part = get_object_or_404(Part, id=part_id)
        form = PartCreateModelForm, PartTypeModelForm(request.POST, instance=part)
        if form.is_valid():
            form.save()
            return redirect("parts:list")
        return render(request, "parts/part_form.html", {"form": form})

class PartDeleteView(View):
    def post(self, request, part_id):
        part = get_object_or_404(Part, id=part_id)
        part.delete()
        return redirect("parts:list")
