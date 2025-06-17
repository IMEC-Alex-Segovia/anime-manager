from Anime import *
import os
import sqlite3
from pathlib import Path

class AnimeManager:
    def __init__(self):
        self.db_path = self.get_db_path()
        self.init_anime_db()
        self.ratings = ["⭐⭐⭐⭐⭐", "⭐⭐⭐⭐", "⭐⭐⭐", "⭐⭐", "⭐", "❓"]
        self.states = ["Viendo", "Terminado", "Por ver", "En pausa"]
        self.genres = ["Acción", "Aventura", "Comedia", "Drama", "Fantasía", "Ciencia Ficción",
            "Romance", "Slice of Life", "Terror", "Misterio", "Thriller", "Supernatural",
            "Deportes", "Musical", "Psicológico", "Mecha", "Harem", "Isekai", "Shounen",
            "Shoujo", "Seinen", "Josei", "Yaoi", "Yuri", "Ecchi", "Hentai" 
        ]
    
    def get_db_path(self):
        appdata_dir = Path(os.getenv("LOCALAPPDATA", Path.home())) / "AnimeManagerApp"
        appdata_dir.mkdir(parents=True, exist_ok=True)
        return appdata_dir / "anime_manager_db.db"
    
    def init_anime_db(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS anime (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                episodes INTEGER NOT NULL,
                rate TEXT NOT NULL,
                state TEXT NOT NULL,
                episode_duration INTEGER NOT NULL,
                genre TEXT NOT NULL
            )
        ''')
        conn.commit()
        conn.close()
    
    def get_anime_ratings(self):
        return self.ratings.copy()
    
    def get_anime_states(self):
        return self.states.copy()
    
    def get_anime_genres(self):
        return self.genres.copy()
    
    def add_new_anime(self, anime: Anime):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO anime (name, episodes, rate, state, episode_duration, genre) VALUES (?, ?, ?, ?, ?, ?)",
            anime.get_anime_data()
        )
        conn.commit()
        conn.close()
    
    def remove_anime(self, anime_id: int):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM anime WHERE id = ?", (anime_id,))
        conn.commit()
        conn.close()

    def get_anime_list(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM anime")
        rows = cursor.fetchall()
        conn.close()
        return [
            Anime(id=row[0], name=row[1], episodes=row[2], rate=row[3], state=row[4], 
                  episode_duration=row[5], genre=row[6]) for row in rows
        ]