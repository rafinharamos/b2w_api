from rest_framework import serializers

from core.models import Planets


class PlanetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Planets
        fields = ["id", "name", "climate", "terrain", "number_of_movie_appearances"]
