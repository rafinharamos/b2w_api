from rest_framework import viewsets

from api.v1.serializers import PlanetSerializer
from core.models import Planets


class PlanetsViewSet(viewsets.ModelViewSet):
    queryset = Planets.objects.all()
    serializer_class = PlanetSerializer
    filter_fields = ["name"]
