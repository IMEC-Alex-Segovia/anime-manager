class Anime:
    def __init__(self, name: str, id = None, episodes: int = 0, rate: str = "❓",
                 state: str = "Por ver", episode_duration: int = 25, genre: list[str] = None):
        self.id = id
        self.name = name                          # nombre del anime
        self.episodes = episodes                  # número de episodios vistos
        self.rate = rate                          # calificación con estrellas del anime (del 1 al 5)
        self.state = state                        # estado del anime (viendo, por ver, en pausa, terminado)
        self.episode_duration = episode_duration  # duración en minutos de cada episodio
        self.genre = genre                        # listado de géneros del anime
    
    def watched_hours(self):
        return round(self.episode_duration * self.episodes / 60, 2)

    def change_watched_episodes(self, current_watched_episodes: int):
        self.episodes = current_watched_episodes

    def change_rate(self, current_rate: str):
        self.rate = current_rate

    def change_state(self, current_state: str):
        self.state = current_state

    def change_episode_duration(self, current_episode_duration: int):
        self.episode_duration = current_episode_duration
    
    def get_anime_data(self):
        return (self.name, self.episodes, self.rate, self.state, self.episode_duration, self.genre)
    
    def get_anime_update_data(self):
        return (self.name, self.episodes, self.rate, self.state, self.episode_duration, self.genre, self.id)
    
    def get_anime_treeview_data(self):
        return (self.name, self.episodes, self.rate, self.genre, self.state)
    