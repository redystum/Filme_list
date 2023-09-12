import sqlite3
import os

from db import migrations
from utils.dbToDict import db_to_json


class Database:

    def __init__(self):
        self.dbPath = os.environ['USERPROFILE'] + '\\FilmList\\data\\' + "database.db"
        self._verify()
        self.db = sqlite3.connect(self.dbPath)
        self.cursor = self.db.cursor()

    def __del__(self):
        self.db.close()

    def _verify(self):
        print(os.path.exists(self.dbPath))
        print(self.dbPath)
        if not os.path.exists(self.dbPath):
            print("Database not found.")
            self._create()
            migrations.migrate(self.dbPath)

    def _create(self):
        os.makedirs(os.path.dirname(self.dbPath), exist_ok=True)
        open(self.dbPath, 'w').close()
        print("Database created.")

    def connected(self) -> bool:
        try:
            self.db.execute("SELECT 1")
            return True
        except sqlite3.OperationalError:
            return False

    def store(self, data: dict):
        """Stores film data in the database."""
        keys = list(data.keys())
        values = list(data.values())
        placeholders = ", ".join(["?"] * len(keys))
        sql = f"INSERT INTO film ( {', '.join(keys)} ) VALUES ( {placeholders} )"
        self.db.execute(sql, values)
        self.db.commit()

    def get_by_imdb(self, imdbId: str):
        """Gets film data from the database."""
        sql = f"SELECT * FROM film WHERE imdbId = '{imdbId}'"
        self.cursor.execute(sql)
        return self.cursor.fetchone()

    def get_by_id(self, id: int):
        """Gets film data from the database."""
        sql = f"SELECT * FROM film WHERE id = '{id}'"
        self.cursor.execute(sql)
        return self.cursor.fetchone()

    def get_all(self):
        """Gets film data from the database."""
        sql = f"SELECT * FROM film ORDER BY id DESC"
        self.cursor.execute(sql)
        fetch = self.cursor.fetchall()
        names = list(map(lambda x: x[0], self.cursor.description))
        film_list = []
        for i in range(len(fetch)):
            fetch[i] = list(fetch[i])
            list_keys = {}
            for j in range(len(fetch[i])):
                list_keys[names[j]] = fetch[i][j]
            film_list.append(list_keys)
        film_list = db_to_json(film_list)
        return film_list
