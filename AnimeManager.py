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
    
    def get_anime_by_id(self, anime_id: int):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM anime WHERE id = ?", (anime_id, ))
        row = cursor.fetchall()[0]
        conn.close()
        return Anime(id=row[0], name=row[1], episodes=row[2], rate=row[3], state=row[4], 
                  episode_duration=row[5], genre=row[6])

    def edit_anime(self, anime: Anime):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("UPDATE anime SET name = ?, episodes = ?, rate = ?, state = ?, episode_duration = ?, genre = ? WHERE id = ?", anime.get_anime_update_data())
        conn.commit()
        conn.close()
    
    def get_watched_hours(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
            SELECT SUM(episodes * episode_duration) AS watched_hours
            FROM anime
            WHERE state IN ('Terminado', 'Viendo', 'En pausa')
        ''')
        watched_hours = cursor.fetchone()
        return round(watched_hours[0] / 60, 2) if watched_hours[0] else None
    
    def get_anime_filtered_list(self, rate="Todas", genre="Todos", state="Todos"):
        filters = {
            "rate": (rate, self.ratings),
            "genre": (genre, self.genres),
            "state": (state, self.states)
        }

        conditions = []
        params = []

        for field, (value, valid_options) in filters.items():
            if value in valid_options:
                conditions.append(f"{field} = ?")
                params.append(value)

        query = "SELECT * FROM anime"
        
        if conditions:
            query += " WHERE " + " AND ".join(conditions)

        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute(query, tuple(params))
        rows = cursor.fetchall()
        conn.close()

        return [
            Anime(id=row[0], name=row[1], episodes=row[2], rate=row[3], state=row[4],
                episode_duration=row[5], genre=row[6]) for row in rows
        ]
                
