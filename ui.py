import eel
import sys

from controllers import filmController

eel.init('web', allowed_extensions=['.js', '.html', '.css'])
startFile = 'index.html'


def start():
    try:
        eel.start(startFile, close_callback=close_callback)  # , mode='mozilla' for firefox
    except OSError:
        try:
            eel.start(startFile, close_callback=close_callback, port=8001)  # , mode='mozilla' for firefox
        except OSError:
            sys.exit()


def close_callback(route, websockets):
    print(route, websockets)
    sys.exit()


@eel.expose
def add_film(title: str):
    filmController.store(title)


@eel.expose
def get_all():
    return filmController.index()


def js_add_film(data: dict):
    print("call js_add_film")
    eel.addFilm(data)


def error(code: int):
    match code:
        case 404:
            eel.start('errors/404.html', close_callback=close_callback, port=8002, block=False)
        case _:
            eel.start('errors/500.html', close_callback=close_callback, port=8002, block=False)
