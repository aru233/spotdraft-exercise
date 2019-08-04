"""Define the services used by the starwars fav core app"""
import requests
from rest_framework.exceptions import NotFound


class SwapiService:
    """Service for interacting with the Start Wars API."""

    BASE_URL = 'https://swapi.co/api/'

    def make_request(self, uri, method, params, post_json=None):
        """ Function to send the HTTP request to SWAPI"""

        if method == 'GET':
            response = requests.get(self.BASE_URL + uri, params=params)
        else:
            response = requests.post(self.BASE_URL + uri, params=params, json=post_json)

        if response.status_code == 404:
            raise NotFound()

        return response.json()

    def get_planets(self, page=1, search=None):
        """Get the list of planets from the SWAPI."""
        params = {
            'page': page,
            'search': search
        }
        response = self.make_request('planets/', 'GET', params=params)
        return response

    def get_movies(self, page=1, search=None):
        """Get the list of movies from the SWAPI."""
        params = {
            'page': page,
            'search': search
        }
        response = self.make_request('films/', 'GET', params=params)
        return response
