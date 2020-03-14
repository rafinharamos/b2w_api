from django.db import models

import requests


class Planets(models.Model):
    class Meta:
        verbose_name = "Planet"
        verbose_name_plural = "Planets"

    name = models.CharField(max_length=20, null=False, blank=False)
    climate = models.CharField(max_length=20, null=False, blank=False)
    terrain = models.CharField(max_length=20, null=False, blank=False)

    @property
    def number_of_movie_appearances(self):
        try:
            response = requests.get(
                f"https://swapi.co/api/planets/?search={self.name}"
            ).json()
            if response["count"] > 0:
                return len(response["results"][0]["films"])
            return 0
        except requests.exceptions.RequestException as e:
            print(e)
            return 0
