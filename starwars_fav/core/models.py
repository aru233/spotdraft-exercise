from django.db import models


class PlanetFavorite(models.Model):
    """Model for saving Planet information to the local Database."""
    external_id = models.IntegerField()
    name = models.CharField(max_length=500)


class MovieFavorite(models.Model):
    """Model for saving the Movie information to the local Database."""
    external_id = models.IntegerField()
    title = models.CharField(max_length=500)
