"""Define the urls of the starwars fav core app."""
from django.urls import path
from starwars_fav.core import views

urlpatterns = [
    path('planets', views.PlanetListView.as_view(), name='list-planets'),
    path('movies', views.MovieListView.as_view(), name='list-movies'),
    path('planets/favorites',
         views.PlanetFavoriteListCreateView.as_view(),
         name='list-create-planet-favorites'),
]
