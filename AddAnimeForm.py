import tkinter as tk
from tkinter import ttk, messagebox
from AnimeManager import *
from Anime import Anime

class AddAnimeForm(tk.Toplevel):
    def __init__(self, master, anime_manager: AnimeManager, on_save_callback):
        super().__init__(master)
        self.title("Agregar Anime")
        self.geometry("350x500")
        self.resizable(False, False)
        self.on_save_callback = on_save_callback
        self.grab_set()

        self.anime_manager = anime_manager
        self.h1_title_font = ("Arial", 14, "bold")
        self.body_font = ("Arial", 11)

        self._setup_form()

    def _setup_form(self):
        tk.Label(self, text="Agregar un nuevo Anime", font=self.h1_title_font).pack(pady=10)

        self.entries = {}

        def add_entry(label_text, key):
            tk.Label(self, text=label_text, font=self.body_font).pack(anchor='w', padx=20, pady=(10, 2))
            entry = tk.Entry(self, font=self.body_font)
            entry.pack(padx=20, fill='x')
            self.entries[key] = entry

        add_entry("Nombre:", "name")
        add_entry("Episodios vistos:", "episodes")
        add_entry("Duración por episodio (min):", "duration")

        # ComboBox: Calificación
        tk.Label(self, text="Calificación:", font=self.body_font).pack(anchor='w', padx=20, pady=(10, 2))
        self.cmb_rate = ttk.Combobox(self, values=self.anime_manager.get_anime_ratings(), state="readonly", font=self.body_font)
        self.cmb_rate.current(0)
        self.cmb_rate.pack(padx=20, fill='x')

        # ComboBox: Estado
        tk.Label(self, text="Estado:", font=self.body_font).pack(anchor='w', padx=20, pady=(10, 2))
        self.cmb_state = ttk.Combobox(self, values=self.anime_manager.get_anime_states(), state="readonly", font=self.body_font)
        self.cmb_state.current(0)
        self.cmb_state.pack(padx=20, fill='x')

        # ComboBox: Género
        tk.Label(self, text="Género:", font=self.body_font).pack(anchor='w', padx=20, pady=(10, 2))
        self.cmb_genre = ttk.Combobox(self, values=self.anime_manager.get_anime_genres(), state="readonly", font=self.body_font)
        self.cmb_genre.current(0)
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
            name=name,
            episodes=int(episodes),
            episode_duration=int(duration),
            rate=rate,
            state=state,
            genre=genre
        )

        self.anime_manager.add_new_anime(anime)  # Asegúrate de tener este método implementado
        self.on_save_callback()
        messagebox.showinfo("Éxito", f"Anime '{name}' agregado correctamente.")
        self.destroy()

