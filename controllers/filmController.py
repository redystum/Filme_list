from request import *
from config import database
import ui


def store(film_id: str):
    """Processes film data and stores it in the database."""
    data = request_film(film_id)
    if data is not None:
        store_data = {
            "imdbId": str(data['id']),
            "imdbLink": str(data['imdb']),
            "type": str(data['contentType']),
            "status": str(data['productionStatus']),
            "name": str(data['title']),
            "image": str(data['image']),
            "images": str(data['images']),
            "plot": str(data['plot']),
            "ratingCount": str(data['rating']['count']),
            "ratingStars": str(data['rating']['star']),
            "awardsWins": str(data['award']['wins']),
            "awardsNominations": str(data['award']['nominations']),
            "contentRating": str(data['contentRating']),
            "genres": str(data['genre']),
            "releaseDetails": str(data['releaseDetailed']),
            "year": str(data['year']),
            "languages": str(data['spokenLanguages']),
            "locations": str(data['filmingLocations']),
            "runtime": str(data['runtime']),
            "runtimeSeconds": str(data['runtimeSeconds']),
            "actors": str(data['actors']),
            "directors": str(data['directors']),
            "topCredits": str(data['top_credits']),
        }
        database.store(store_data)
        store_data['genres'] = data['genre']
        ui.js_add_film(store_data)


def search(title: str):
    """Requests film data from the API."""
    search(title)


def index():
    """Gets all film data from the database."""
    data = database.get_all()
    for i in range(len(data)):
        data[i]['images'].insert(0, data[i]['image'])
        data[i]['image'] = data[i]['images'][data[i]['selectedImage']]

    return data
