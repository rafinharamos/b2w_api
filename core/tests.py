import responses

import requests
from django.test import TestCase
from .models import Planets


class FunctionalTest(TestCase):
    """Functional tests"""

    def setUp(self):
        Planets.objects.create(name="another_planet", climate="arid", terrain="desert")
        Planets.objects.create(name="any_planet", climate="any", terrain="any")

    def test_request_home(self):
        response = self.client.get("/")
        self.assertEqual(200, response.status_code)
        self.assertEqual(
            {"api/v1/planets": "http://testserver/api/v1/planets/"}, response.json()
        )

    def test_request_planets(self):
        response_planets = self.client.get("/api/v1/planets/")
        self.assertEqual(response_planets.status_code, 200)

        self.assertEqual(
            [
                {
                    "id": 1,
                    "name": "another_planet",
                    "number_of_movie_appearances": 0,
                    "climate": "arid",
                    "terrain": "desert",
                },
                {
                    "id": 2,
                    "name": "any_planet",
                    "climate": "any",
                    "terrain": "any",
                    "number_of_movie_appearances": 0,
                },
            ],
            response_planets.json(),
        )

    def test_search_by_name(self):
        response_by_name = self.client.get("/api/v1/planets/?name=another_planet")
        self.assertEqual(
            [
                {
                    "id": 1,
                    "name": "another_planet",
                    "number_of_movie_appearances": 0,
                    "climate": "arid",
                    "terrain": "desert",
                }
            ],
            response_by_name.json(),
        )

    def test_name_not_found(self):
        response_by_name = self.client.get("/api/v1/planets/?name=not_exist")
        self.assertEqual([], response_by_name.json())


class IntegrationTest(TestCase):
    """Integration tests"""

    def setUp(self):
        Planets.objects.create(name="Alderaan", climate="arid", terrain="desert")

    def test_number_of_movie_appearances(self):
        response_http = requests.get("https://swapi.co/api/planets/?search=Alderaan")
        self.assertEqual(200, response_http.status_code)
        self.assertEqual(2, len(response_http.json()["results"][0]["films"]))

    @responses.activate
    def test_number_of_movie_appearances_fail_http(self):
        responses.add(
            responses.GET,
            "https://swapi.co/api/planets/?search=Alderaan",
            json={"error": "not found"},
            status=404,
        )

        resp = requests.get("https://swapi.co/api/planets/?search=Alderaan")

        self.assertEqual(resp.json(), {"error": "not found"})

        self.assertEqual(
            responses.calls[0].request.url,
            "https://swapi.co/api/planets/?search=Alderaan",
        )
        self.assertEqual(responses.calls[0].response.text, '{"error": "not found"}')
