from ninja import NinjaAPI
from .models import Part
from .schemas import PartSchema


part_api = NinjaAPI()


@part_api.get("/", response=list[PartSchema])
def get_parts(request):
    if request.user.isLoggedIn:
        return Part.objects.all()
    return []
