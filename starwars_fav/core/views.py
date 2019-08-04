"""Define the views of the starwars fav core app."""
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from starwars_fav.core.serializers import PaginatedMovieSerializer, PaginatedPlanetSerializer
from starwars_fav.core.services import SwapiService


class PlanetListView(GenericAPIView):
    """View for listing the planets from the SWAPI."""

    serializer_class = PaginatedPlanetSerializer

    def get(self, request):
        """Return the list of planets for the requested page."""

        # Call the service to get the result
        service = SwapiService()
        result = service.get_planets(page=request.query_params.get('page', 1))

        # Call the serializer and return the response
        serializer = self.get_serializer(result)
        return Response(serializer.data)


class MovieListView(GenericAPIView):
    """View for listing the movies from the SWAPI."""

    serializer_class = PaginatedMovieSerializer

    def get(self, request):
        """Return the list of planets for the requested page."""

        # Call the service to get the result
        service = SwapiService()
        result = service.get_movies(page=request.query_params.get('page', 1))

        # Call the serializer and return the response
        serializer = self.get_serializer(result)
        return Response(serializer.data)