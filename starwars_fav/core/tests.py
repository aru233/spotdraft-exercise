"""Add the test cases for the Startwars Fav Core app"""
from rest_framework.test import APITestCase


class CoreTestCases(APITestCase):

    def test_list_planets(self):
        """Test the list planets endpoint."""

        # Get the list of planets
        response = self.client.get('/api/planets')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['count'], 61)
        self.assertIsNotNone(response.json()['next'])
        self.assertIsNone(response.json()['previous'])
        self.assertEqual(response.json()['results'][0]['name'], 'Alderaan')

        # Get the next page of planets list
        response = self.client.get('/api/planets', {'page': 2})
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.json()['next'])
        self.assertIsNotNone(response.json()['previous'])
        self.assertEqual(response.json()['results'][0]['name'], 'Utapau')

        # Test the searching of planets by name
        response = self.client.get('/api/planets', {'search': 'yavin'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['count'], 1)
        self.assertEqual(response.json()['results'][0]['name'], 'Yavin IV')

    def test_list_movies(self):
        """Test the list movies endpoint."""

        # Get the list of planets
        response = self.client.get('/api/movies')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['count'], 7)
        self.assertIsNone(response.json()['next'])
        self.assertIsNone(response.json()['previous'])
        self.assertEqual(response.json()['results'][0]['title'], 'A New Hope')

        # Get the next page of planets list
        response = self.client.get('/api/movies', {'page': 2})
        self.assertEqual(response.status_code, 404)

        # Test the searching of planets by name
        response = self.client.get('/api/movies', {'search': 'attack'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['count'], 1)
        self.assertEqual(response.json()['results'][0]['title'], 'Attack of the Clones')

    def test_add_planet(self):
        """Test the endpoint for adding a planet to favorites."""

        # Get the list of planets
        response = self.client.get('/api/planets')
        self.assertEqual(response.status_code, 200)
        planet = response.json()['results'][2]

        # Add  the planet to favorites
        response = self.client.post(
            '/api/planets/favorites', data={'external_id': planet['id'], 'name': planet['name']})
        self.assertEqual(response.status_code, 201)

        # Check that the favorite tag is set
        response = self.client.get('/api/planets')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.json()['results'][2]['is_favorite'])

        # Get the list of favorites
        response = self.client.get('/api/planets/favorites')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['count'], 1)
        self.assertEqual(response.json()['results'][0]['name'], planet['name'])

    def test_add_movie(self):
        """Test the endpoint for adding a movie to favorites."""
        # Get the list of planets
        response = self.client.get('/api/movies')
        self.assertEqual(response.status_code, 200)
        movie = response.json()['results'][2]

        # Add  the planet to favorites
        response = self.client.post(
            '/api/movies/favorites', data={'external_id': movie['id'], 'title': movie['title']})
        self.assertEqual(response.status_code, 201)

        # Check that the favorite tag is set
        response = self.client.get('/api/movies')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.json()['results'][2]['is_favorite'])

        # Get the list of favorites
        response = self.client.get('/api/movies/favorites')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['count'], 1)
        self.assertEqual(response.json()['results'][0]['title'], movie['title'])
