"""Define the views of the starwars fav core app."""
from rest_framework.generics import GenericAPIView, ListCreateAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from starwars_fav.core.serializers import (
    PaginatedMovieSerializer,
    PaginatedPlanetSerializer,
    PlanetFavoriteSerializer,
    MovieFavoriteSerializer
)
from starwars_fav.core.models import PlanetFavorite, MovieFavorite
from starwars_fav.core.services import SwapiService


class PlanetListView(GenericAPIView):
    """View for listing the planets from the SWAPI."""

    serializer_class = PaginatedPlanetSerializer

    def get(self, request):
        """Return the list of planets for the requested page."""

        # Call the service to get the result
        service = SwapiService()
        result = service.get_planets(
            page=request.query_params.get('page', 1), search=request.query_params.get('search'))

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
        result = service.get_movies(
            page=request.query_params.get('page', 1), search=request.query_params.get('search'))

        # Call the serializer and return the response
        serializer = self.get_serializer(result)
        return Response(serializer.data)


class PlanetFavoriteListCreateView(ListCreateAPIView):
    """View for listing and creating Planet Favorites."""

    serializer_class = PlanetFavoriteSerializer
    queryset = PlanetFavorite.objects.order_by('name')
    pagination_class = PageNumberPagination


class MovieFavoriteListCreateView(ListCreateAPIView):
    """View for listing and creating Movie Favorites."""

    serializer_class = MovieFavoriteSerializer
    queryset = MovieFavorite.objects.order_by('title')
    pagination_class = PageNumberPagination
