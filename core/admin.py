from django.contrib import admin

from core.models import Planets


class PlanetsAdmin(admin.ModelAdmin):
    list_display = ("name", "climate", "terrain", "number_of_movie_appearances")


admin.site.register(Planets, PlanetsAdmin)
