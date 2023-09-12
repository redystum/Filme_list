import requests

from config import api


def request_film(film_id: str):
    """Requests film data from the API."""
    try:
        return requests.get(api + "title/" + film_id).json()
    except requests.exceptions.ConnectionError:
        return None


def search(title: str):
    """Requests film data from the API."""
    try:
        response = requests.get(api + "search?query=" + title)
        return response.json()['results']
    except requests.exceptions.ConnectionError:
        return None
