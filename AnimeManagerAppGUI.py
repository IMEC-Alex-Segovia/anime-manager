import tkinter as tk
from tkinter import ttk

class AnimeAppGUI:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Lista de Animes")
        self.root.geometry("700x500")
        self.root.resizable(False, False)
        self.h1_title_font = ("Arial", 14, "bold")
        self.body_font = ("Arial", 11)
        self.setup_ui()
    
    def setup_ui(self):
        # ===== TITLE =====
        title_label = ttk.Label(self.root, text="Listado de Animes", font=self.h1_title_font)
        title_label.pack(pady=5)

        # ===== SEARCH ANIME =====
        search_frame = ttk.Frame(self.root)
        search_frame.pack(pady=5)
        search_label = ttk.Label(search_frame, text="Anime:", font=self.body_font)
        search_label.pack(side=tk.LEFT, padx=5)
        self.search_entry = ttk.Entry(search_frame, width=61, font=self.body_font)
        self.search_entry.pack(side=tk.LEFT, padx=5)
        btn_search = ttk.Button(search_frame, text="Buscar")
        btn_search.pack(side=tk.LEFT, padx=5)

        # ===== FILTER =====
        cmb_gen_values = [
            "Todos", "Acción", "Aventura", "Comedia", "Drama", "Fantasía", "Ciencia Ficción",
            "Romance", "Slice of Life", "Terror", "Misterio", "Thriller", "Supernatural",
            "Deportes", "Musical", "Psicológico", "Mecha", "Harem", "Isekai", "Shounen",
            "Shoujo", "Seinen", "Josei", "Yaoi", "Yuri", "Ecchi", "Hentai" 
        ]
        cmb_cal_values = ["Todas", "⭐⭐⭐⭐⭐", "⭐⭐⭐⭐", "⭐⭐⭐", "⭐⭐", "⭐", "❓"]
        cmb_sta_values = ["Todos", "Viendo", "Terminado", "Por ver", "En pausa"]
        filter_frame = ttk.Frame(self.root)
        filter_frame.pack(pady=5)
        cal_label = ttk.Label(filter_frame, text="Calificación:", font=self.body_font)
        cal_label.pack(side=tk.LEFT, padx=5)
        self.cmb_cal = ttk.Combobox(filter_frame, values=cmb_cal_values, width=15, state='readonly')
        self.cmb_cal.current(0)
        self.cmb_cal.pack(side=tk.LEFT, padx=5)
        gen_label = ttk.Label(filter_frame, text="Género:", font=self.body_font)
        gen_label.pack(side=tk.LEFT, padx=5)
        self.cmb_gen = ttk.Combobox(filter_frame, values=cmb_gen_values, width=15, state='readonly')
        self.cmb_gen.current(0)
        self.cmb_gen.pack(side=tk.LEFT, padx=5)
        sta_label = ttk.Label(filter_frame, text="Estado:", font=self.body_font)
        sta_label.pack(side=tk.LEFT, padx=5)
        self.cmb_sta = ttk.Combobox(filter_frame, values=cmb_sta_values, width=10, state='readonly')
        self.cmb_sta.current(0)
        self.cmb_sta.pack(side=tk.LEFT, padx=5)
        btn_filter = ttk.Button(filter_frame, text="Filtrar")
        btn_filter.pack(side=tk.LEFT, padx=5)

        # ===== ANIME LIST =====
        anime_list_frame = ttk.Frame(self.root)
        anime_list_frame.pack(pady=5)
        self.setup_anime_list(anime_list_frame)

        # ===== BUTTONS =====
        btns_padx = 10
        buttons_frame = ttk.Frame(self.root)
        buttons_frame.pack(pady=btns_padx)
        btn_add = ttk.Button(buttons_frame, text="Agregar Anime")
        btn_add.pack(side=tk.LEFT, padx=btns_padx)
        btn_remove = ttk.Button(buttons_frame, text="Eliminar Anime")
        btn_remove.pack(side=tk.LEFT, padx=btns_padx)
        btn_edit = ttk.Button(buttons_frame, text="Editar información")
        btn_edit.pack(side=tk.LEFT, padx=btns_padx)
    
    def setup_anime_list(self, list_frame: ttk.Frame):
        cols = ("name", "caps", "cal", "gen", "state")
        self.tree_anime_list = ttk.Treeview(list_frame, columns=cols, show='headings', height=15)
        self.tree_anime_list.pack()
        # ===== HEADINGS =====
        self.tree_anime_list.heading("name", text="Nombre")
        self.tree_anime_list.heading("caps", text="Capítulos")
        self.tree_anime_list.heading("cal", text="Calificación")
        self.tree_anime_list.heading("gen", text="Género")
        self.tree_anime_list.heading("state", text="Estado")
        # ===== COLUMNS =====
        self.tree_anime_list.column("name", width=280)
        self.tree_anime_list.column("caps", width=70)
        self.tree_anime_list.column("cal", width=100)
        self.tree_anime_list.column("gen", width=100)
        self.tree_anime_list.column("state", width=100)