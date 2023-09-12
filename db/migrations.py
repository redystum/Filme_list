import sqlite3


def migrate(db_path: str) -> bool:
    """Creates the database and tables."""
    try:
        con = sqlite3.connect(db_path)
        cur = con.cursor()
        film_table(cur)
        con.commit()
        con.close()
    except sqlite3.Error as e:
        print(e)
        return False
    return True


def film_table(cur: sqlite3.Cursor):
    cur.execute("""CREATE TABLE IF NOT EXISTS film (
        /* internal fields */
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        imdbId TEXT NOT NULL,
        imdbLink TEXT NOT NULL,
        type TEXT NOT NULL,
        status TEXT NOT NULL,
        name TEXT NOT NULL,
        image TEXT NOT NULL,
        images TEXT NOT NULL,
        plot TEXT NOT NULL,
        ratingCount INTEGER NOT NULL,
        ratingStars REAL NOT NULL,
        awardsWins INTEGER NOT NULL,
        awardsNominations INTEGER NOT NULL,
        contentRating TEXT NOT NULL,
        genres TEXT NOT NULL,
        releaseDetails TEXT NOT NULL,
        year INTEGER NOT NULL,
        languages TEXT NOT NULL,
        locations TEXT NOT NULL,
        runtime TEXT NOT NULL,
        runtimeSeconds INTEGER NOT NULL,
        actors TEXT NOT NULL,
        directors TEXT NOT NULL,
        topCredits TEXT NOT NULL,
        /* user fields */
        selectedImage INTEGER NOT NULL DEFAULT '0',
        userRating INTEGER,
        userReview TEXT,
        userWatched BOOLEAN,
        userWatchedDate TEXT
    )""")
