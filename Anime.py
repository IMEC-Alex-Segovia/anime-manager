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
    
    def get_anime_data(self):
        return (self.name, self.episodes, self.rate, self.state, self.episode_duration, self.genre)
    
    def get_anime_update_data(self):
        return (self.name, self.episodes, self.rate, self.state, self.episode_duration, self.genre, self.id)
    
    def get_anime_treeview_data(self):
        return (self.name, self.episodes, self.rate, self.genre, self.state)
    