"""Define the utility methods for the Starwars Fav Core app."""
import re


def get_id_from_url(url):
    """Get the ID from the SWAPI URL."""
    swapi_id = None
    search_id = re.search(r'/([0-9]+)/$', url)
    if search_id:
        swapi_id = int(search_id.group(1))
    return swapi_id
