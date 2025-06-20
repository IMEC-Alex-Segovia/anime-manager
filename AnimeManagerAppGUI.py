import tkinter as tk
from tkinter import ttk
from AnimeManager import *
from AnimeListFrame import *

class AnimeAppGUI:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Anime Manager")
        self.width = 700
        self.height = 515
        self.root.geometry(f"{self.width}x{self.height}")
        self.root.resizable(False, False)
        self.h1_title_font = ("Arial", 14, "bold")
        self.body_font = ("Arial", 11)
        
        self.setup_ui()
    
    def setup_ui(self):
        self.notebook = ttk.Notebook(self.root, width=self.width, height=self.height)
        self.notebook.pack(expand=True)

        self.anime_manager_list = AnimeListFrame(self.notebook, root=self.root, height=self.height, width=self.width)
        self.anime_manager_list.pack(fill="both", expand=True)

        self.anime_manager_config = tk.Label(self.notebook, height=self.height, width=self.width)
        self.anime_manager_config.pack(fill="both", expand=True)

        self.notebook.add(self.anime_manager_list, text="Lista de Anime")
        self.notebook.add(self.anime_manager_config, text="Configuración")