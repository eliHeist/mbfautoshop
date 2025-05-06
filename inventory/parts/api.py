from ninja import NinjaAPI, Router
from .models import Part
from .schemas import PartSchema


part_api = Router()


@part_api.get("/", response=list[PartSchema], url_name="get_all_parts")
def get_parts(request):
    if request.user:
        return Part.objects.all()
    return []

@part_api.get("/search/", response=list[PartSchema], url_name="search_parts")
def get_parts(request):
    query = request.GET.get("q")
    if request.user and query:
        number_matches = Part.objects.filter(part_number__icontains=query)
        name_matches = Part.objects.filter(name__icontains=query)
        type_matches = Part.objects.filter(type__name__icontains=query)
        
        final = []
        for match in number_matches:
            if match not in final:
                final.append(match)
        for match in name_matches:
            if match not in final:
                final.append(match)
        for match in type_matches:
            if match not in final:
                final.append(match)
        
        return final
    return []


@part_api.get("/{pk}/", response=PartSchema, url_name="get_part")
def get_part(request, pk):
    return Part.objects.get(pk=pk)
