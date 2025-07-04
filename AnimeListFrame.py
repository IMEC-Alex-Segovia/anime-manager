import tkinter as tk
from tkinter import ttk, messagebox
from AnimeManager import *
from AddAnimeForm import *
from EditAnimeForm import *
class AnimeListFrame(tk.Frame):
    def __init__(self, master, root: tk.Tk, height: int, width: int):
        super().__init__(master, height=height, width=width)
        self.root = root
        self.anime_manager = AnimeManager()
        self.h1_title_font = ("Arial", 14, "bold")
        self.body_font = ("Arial", 11)

        # === Listas de widgets para personalización posterior ===
        self.button_list = []
        self.label_list = []
        self.entry_list = []
        self.combobox_list = []

        # ===== TITLE =====
        title_label = ttk.Label(self, text="Listado de Animes", font=self.h1_title_font)
        title_label.pack(pady=5)
        self.label_list.append(title_label)

        # ===== SEARCH ANIME =====
        search_frame = ttk.Frame(self)
        search_frame.pack(pady=5)

        search_label = ttk.Label(search_frame, text="Anime:", font=self.body_font)
        search_label.pack(side=tk.LEFT, padx=5)
        self.label_list.append(search_label)

        self.search_entry = ttk.Entry(search_frame, width=61, font=self.body_font)
        self.search_entry.pack(side=tk.LEFT, padx=5)
        self.entry_list.append(self.search_entry)

        btn_search = ttk.Button(search_frame, text="Buscar", command=self.search_anime_by_name)
        btn_search.pack(side=tk.LEFT, padx=5)
        self.button_list.append(btn_search)

        # ===== FILTER =====
        cmb_gen_values = ["Todos"] + self.anime_manager.get_anime_genres()
        cmb_cal_values = ["Todas"] + self.anime_manager.get_anime_ratings()
        cmb_sta_values = ["Todos"] + self.anime_manager.get_anime_states()

        filter_frame = ttk.Frame(self)
        filter_frame.pack(pady=5)

        cal_label = ttk.Label(filter_frame, text="Calificación:", font=self.body_font)
        cal_label.pack(side=tk.LEFT, padx=5)
        self.label_list.append(cal_label)

        self.cmb_cal = ttk.Combobox(filter_frame, values=cmb_cal_values, width=15, state='readonly')
        self.cmb_cal.current(0)
        self.cmb_cal.pack(side=tk.LEFT, padx=5)
        self.combobox_list.append(self.cmb_cal)

        gen_label = ttk.Label(filter_frame, text="Género:", font=self.body_font)
        gen_label.pack(side=tk.LEFT, padx=5)
        self.label_list.append(gen_label)

        self.cmb_gen = ttk.Combobox(filter_frame, values=cmb_gen_values, width=15, state='readonly')
        self.cmb_gen.current(0)
        self.cmb_gen.pack(side=tk.LEFT, padx=5)
        self.combobox_list.append(self.cmb_gen)

        sta_label = ttk.Label(filter_frame, text="Estado:", font=self.body_font)
        sta_label.pack(side=tk.LEFT, padx=5)
        self.label_list.append(sta_label)

        self.cmb_sta = ttk.Combobox(filter_frame, values=cmb_sta_values, width=10, state='readonly')
        self.cmb_sta.current(0)
        self.cmb_sta.pack(side=tk.LEFT, padx=5)
        self.combobox_list.append(self.cmb_sta)

        btn_filter = ttk.Button(filter_frame, text="Filtrar", command=self.get_filtered_anime_treeview)
        btn_filter.pack(side=tk.LEFT, padx=5)
        self.button_list.append(btn_filter)

        # ===== ANIME LIST =====
        anime_list_frame = ttk.Frame(self)
        anime_list_frame.pack(pady=5)
        self.setup_anime_list(anime_list_frame)
        self.update_anime_treeview()

        # ===== BUTTONS =====
        btns_padx = 10
        buttons_frame = ttk.Frame(self)
        buttons_frame.pack(pady=btns_padx)

        btn_add = ttk.Button(buttons_frame, text="Agregar Anime", command=self.open_add_anime_window)
        btn_add.pack(side=tk.LEFT, padx=btns_padx)
        self.button_list.append(btn_add)

        btn_remove = ttk.Button(buttons_frame, text="Eliminar Anime", command=self.remove_anime)
        btn_remove.pack(side=tk.LEFT, padx=btns_padx)
        self.button_list.append(btn_remove)

        btn_edit = ttk.Button(buttons_frame, text="Editar información", command=self.open_edit_anime_window)
        btn_edit.pack(side=tk.LEFT, padx=btns_padx)
        self.button_list.append(btn_edit)

        btn_hrs = ttk.Button(buttons_frame, text="Horas vistas", command=self.show_watched_hours)
        btn_hrs.pack(side=tk.LEFT, padx=btns_padx)
        self.button_list.append(btn_hrs)
    
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
        
    def update_anime_treeview(self):
        for item in self.tree_anime_list.get_children():
            self.tree_anime_list.delete(item)
        
        for anime in self.anime_manager.get_anime_list():
            self.tree_anime_list.insert("", "end", iid=str(anime.id), values=anime.get_anime_treeview_data())

    def remove_anime(self):
        selected_anime = self.tree_anime_list.selection()
        if selected_anime:
            confirm = messagebox.askokcancel("Confirmación", "¿Estás seguro de querer borrar este Anime?")
            if confirm:
                self.anime_manager.remove_anime(selected_anime[0])
                self.update_anime_treeview()
                messagebox.showinfo("Éxito", "Anime borrado exitosamente")
        else:
            messagebox.showwarning("Advertencia", "Seleccione un Anime para borrar")

    # ===== NUEVA VENTANA PARA AGREGAR ANIME =====
    def open_add_anime_window(self):
        AddAnimeForm(self.root, self.anime_manager, on_save_callback=self.update_anime_treeview)        

    def open_edit_anime_window(self):
        selected_anime = self.tree_anime_list.selection()
        if selected_anime:
            EditAnimeForm(self.root, anime_manager=self.anime_manager, anime_id=selected_anime[0], 
                          on_save_callback=self.update_anime_treeview)
        else:
            messagebox.showwarning("Advertencia", "Seleccione un Anime para editar")
    
    def show_watched_hours(self):
        watched_hours = self.anime_manager.get_watched_hours()
        if watched_hours is None:
            messagebox.showinfo("Tiempo viendo Anime", "Parece que aun no haz visto Anime")
            return
        message = f"¡Usted ha visto {watched_hours} horas de Anime!"
        if (watched_hours / 24) > 1:
            message += f"\nEso equivale a {round(watched_hours / 24, 2)} días."
        messagebox.showinfo("Tiempo viendo Anime", message)
    
    def get_filtered_anime_treeview(self):
        for item in self.tree_anime_list.get_children():
            self.tree_anime_list.delete(item)
        
        rate = self.cmb_cal.get()
        genre = self.cmb_gen.get()
        state = self.cmb_sta.get()

        for anime in self.anime_manager.get_anime_filtered_list(rate, genre, state):
            self.tree_anime_list.insert("", "end", iid=str(anime.id), values=anime.get_anime_treeview_data())
        
        messagebox.showinfo("Información", "Se han aplicado los filtros a la lista de Anime")
    
    def search_anime_by_name(self):
        anime_name = self.search_entry.get().strip()
        if anime_name:
            for item in self.tree_anime_list.get_children():
                self.tree_anime_list.delete(item)
            
            animes = self.anime_manager.get_anime_by_name(anime_name)
            if animes:
                for anime in animes:
                    self.tree_anime_list.insert("", "end", iid=str(anime.id), values=anime.get_anime_treeview_data())
            else:
                messagebox.showinfo("Información", f"No se encontraron Animes con el nombre {anime_name}")
        else:
            messagebox.showinfo("Información", "Escriba el nombre de un Anime")
        self.search_entry.delete(0, "end")
