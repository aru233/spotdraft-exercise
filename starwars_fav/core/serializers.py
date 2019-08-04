"""Define the serializers of the starwars fav core app."""
from django.urls import reverse
from rest_framework import serializers


class PaginatedSerializer(serializers.Serializer):
    """Custom Pagination Serializer as we are rendering directly from SWAPI."""
    count = serializers.IntegerField()
    next = serializers.SerializerMethodField()
    previous = serializers.SerializerMethodField()
    route_name = None

    def get_next(self, obj):
        """Replace the SWAPI URL with our URL."""
        next_url = None
        if obj['next']:
            next_url = self.context['request'].build_absolute_uri(reverse(self.route_name))
            next_url = f'{next_url}?{obj["next"].split("?")[-1]}'
        return next_url

    def get_previous(self, obj):
        """Replace the SWAPI URL with our URL."""
        previous_url = None
        if obj['previous']:
            previous_url = self.context['request'].build_absolute_uri(
                reverse(reverse(self.route_name)))
            previous_url = f'{previous_url}?{obj["previous"].split("?")[-1]}'
        return previous_url


class PlanetSerializer(serializers.Serializer):
    """Serializer for the Planet Resource."""
    name = serializers.CharField(max_length=500)


class PaginatedPlanetSerializer(PaginatedSerializer):
    """Custom Pagination Serializer as we are rendering directly from SWAPI."""
    results = PlanetSerializer(many=True)
    route_name = 'list-planets'


class MovieSerializer(serializers.Serializer):
    """Serializer for the Movie Resource."""
    title = serializers.CharField(max_length=500)


class PaginatedMovieSerializer(PaginatedSerializer):
    """Custom Pagination Serializer as we are rendering directly from SWAPI."""
    results = MovieSerializer(many=True)
    route_name = 'list-movies'
