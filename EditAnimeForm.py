import tkinter as tk
from tkinter import ttk, messagebox
from AnimeManager import *
from Anime import Anime

class EditAnimeForm(tk.Toplevel):
    def __init__(self, master, anime_manager: AnimeManager, anime_id: int, on_save_callback):
        super().__init__(master)
        self.title("Editar Anime")
        self.geometry("350x500")
        self.resizable(False, False)
        self.on_save_callback = on_save_callback
        self.grab_set()

        self.anime_manager = anime_manager
        self.anime_id = anime_id
        self.anime = self.anime_manager.get_anime_by_id(self.anime_id)
        self.h1_title_font = ("Arial", 14, "bold")
        self.body_font = ("Arial", 11)

        self._setup_form()

    def _setup_form(self):
        tk.Label(self, text="Editar Anime", font=self.h1_title_font).pack(pady=10)

        self.entries = {}

        def add_entry(label_text, key):
            tk.Label(self, text=label_text, font=self.body_font).pack(anchor='w', padx=20, pady=(10, 2))
            entry = tk.Entry(self, font=self.body_font)
            entry.pack(padx=20, fill='x')
            self.entries[key] = entry

        add_entry("Nombre:", "name")
        add_entry("Episodios vistos:", "episodes")
        add_entry("Duración por episodio (min):", "duration")

        self.entries["name"].insert(0, self.anime.name)
        self.entries["episodes"].insert(0, self.anime.episodes)
        self.entries["duration"].insert(0, self.anime.episode_duration)

        # ComboBox: Calificación
        tk.Label(self, text="Calificación:", font=self.body_font).pack(anchor='w', padx=20, pady=(10, 2))
        self.cmb_rate = ttk.Combobox(self, values=self.anime_manager.get_anime_ratings(), state="readonly", font=self.body_font)
        self.cmb_rate.current(self.anime_manager.get_anime_ratings().index(self.anime.rate))
        self.cmb_rate.pack(padx=20, fill='x')

        # ComboBox: Estado
        tk.Label(self, text="Estado:", font=self.body_font).pack(anchor='w', padx=20, pady=(10, 2))
        self.cmb_state = ttk.Combobox(self, values=self.anime_manager.get_anime_states(), state="readonly", font=self.body_font)
        self.cmb_state.current(self.anime_manager.get_anime_states().index(self.anime.state))
        self.cmb_state.pack(padx=20, fill='x')

        # ComboBox: Género
        tk.Label(self, text="Género:", font=self.body_font).pack(anchor='w', padx=20, pady=(10, 2))
        self.cmb_genre = ttk.Combobox(self, values=self.anime_manager.get_anime_genres(), state="readonly", font=self.body_font)
        self.cmb_genre.current(self.anime_manager.get_anime_genres().index(self.anime.genre))
        self.cmb_genre.pack(padx=20, fill='x')

        # Botón de guardar
        ttk.Button(self, text="Guardar", command=self._save_anime).pack(pady=20)

    def _save_anime(self):
        name = self.entries["name"].get().strip()
        episodes = self.entries["episodes"].get().strip()
        duration = self.entries["duration"].get().strip()
        rate = self.cmb_rate.get()
        state = self.cmb_state.get()
        genre = self.cmb_genre.get()

        # Validación básica
        if not name or not episodes.isdigit() or not duration.isdigit():
            messagebox.showerror("Error", "Asegúrate de que los campos nombre, episodios y duración sean válidos.")
            return

        anime = Anime(
            id=self.anime_id,
            name=name,
            episodes=int(episodes),
            episode_duration=int(duration),
            rate=rate,
            state=state,
            genre=genre
        )

        self.anime_manager.edit_anime(anime) 
        self.on_save_callback()
        messagebox.showinfo("Éxito", f"Anime '{name}' editado correctamente.")
        self.destroy()