"""Define the serializers of the starwars fav core app."""
from django.urls import reverse
from rest_framework import serializers

from starwars_fav.core.utils import get_id_from_url
from starwars_fav.core.models import PlanetFavorite, MovieFavorite


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
            previous_url = self.context['request'].build_absolute_uri(reverse(self.route_name))
            previous_url = f'{previous_url}?{obj["previous"].split("?")[-1]}'
        return previous_url


class PlanetSerializer(serializers.Serializer):
    """Serializer for the Planet Resource."""
    id = serializers.SerializerMethodField()
    name = serializers.CharField(max_length=500)
    is_favorite = serializers.BooleanField(default=False)

    def get_id(self, obj):
        """Get the ID from the SWAPI URL, needed for saving favorites."""
        return get_id_from_url(obj.get('url'))


class PaginatedPlanetSerializer(PaginatedSerializer):
    """Custom Pagination Serializer as we are rendering directly from SWAPI."""
    results = PlanetSerializer(many=True)
    route_name = 'list-planets'

    def to_representation(self, instance):
        """Override the serialization to include is_favorite field."""
        ret = super().to_representation(instance)

        # For each planet in the result check if a favorite exists and populate is_favorite
        planet_ids = [m['id'] for m in ret['results']]
        fav_planets = [
            m.external_id for m in PlanetFavorite.objects.filter(external_id__in=planet_ids)]
        for planet in ret['results']:
            planet['is_favorite'] = True if planet['id'] in fav_planets else False
        return ret


class MovieSerializer(serializers.Serializer):
    """Serializer for the Movie Resource."""
    id = serializers.SerializerMethodField()
    title = serializers.CharField(max_length=500)
    is_favorite = serializers.BooleanField(default=False)

    def get_id(self, obj):
        """Get the ID from the SWAPI URL"""
        return get_id_from_url(obj.get('url'))


class PaginatedMovieSerializer(PaginatedSerializer):
    """Custom Pagination Serializer as we are rendering directly from SWAPI."""
    results = MovieSerializer(many=True)
    route_name = 'list-movies'

    def to_representation(self, instance):
        """Override the serialization to include is_favorite field."""
        ret = super().to_representation(instance)

        # For each movie in the result check if a favorite exists and populate is_favorite
        movie_ids = [m['id'] for m in ret['results']]
        fav_movies = [
            m.external_id for m in MovieFavorite.objects.filter(external_id__in=movie_ids)]
        for movie in ret['results']:
            movie['is_favorite'] = True if movie['id'] in fav_movies else False
        return ret


class PlanetFavoriteSerializer(serializers.ModelSerializer):
    """Serializer for the Planet Favorite Resource."""
    external_id = serializers.IntegerField(write_only=True)

    class Meta:
        """Options for the Planet Favorite Serializer."""
        model = PlanetFavorite
        fields = ('name', 'external_id')


class MovieFavoriteSerializer(serializers.ModelSerializer):
    """Serializer for the Movie Favorite Resource."""
    external_id = serializers.IntegerField(write_only=True)

    class Meta:
        """Options for the Planet Favorite Serializer."""
        model = MovieFavorite
        fields = ('title', 'external_id')
