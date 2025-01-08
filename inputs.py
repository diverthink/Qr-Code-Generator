import tkinter as tk
import tkinter.colorchooser as tkc
import tkinter.ttk as ttk
import tkinter.filedialog as filedialog

import qr_generator

def choose_color(root, entry):
    color = tkc.askcolor(parent=root, title="Choose color", initialcolor="#033E77")
    entry.delete(0, tk.END)
    entry.insert(0, color[1])

def filepath(root, entry):
    files = filedialog.askopenfilenames(parent=root, title="Select files", multiple=True)
    entry.delete(0, tk.END)
    entry.insert(0, files[0])

def save_dir(root, entry):
    dirs = filedialog.askdirectory(parent=root, title='Select directories')
    entry.delete(0, tk.END)
    entry.insert(0, dirs)



def makeform(root):
    entries = {}

    
    # Eingabemaske URL
    label_url = tk.Label(root, width = 15, text="Deine URL", anchor="w")
    ent_url = tk.Entry(root)
    label_url.grid(row=0, column=0, padx=5, pady=5, sticky="w")
    ent_url.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
    entries["url"] = ent_url
    
    # Farbauswahl Punkte
    label_color_points = tk.Label(root, width=15, text="Punktfarbe", anchor="w")
    ent_color_points = tk.Entry(root)
    button_color_points = tk.Button(root, text='Farbe der Punkte', command=lambda: choose_color(root, ent_color_points))
    label_color_points.grid(row=1, column=0, padx=5, pady=5, sticky="w")
    ent_color_points.grid(row=1, column=1, padx=5, pady=5, sticky="ew")
    button_color_points.grid(row=1, column=2, padx=5, pady=5, sticky="ew")
    entries["color"] = ent_color_points
    
    # Farbauswahl Hintergrundfarbe
    label_back_color = tk.Label(root, width=15, text="Hintergrundfarbe", anchor="w")
    ent_back_color = tk.Entry(root)
    button_back_color = tk.Button(root, text='Farbe des Hintergrunds', command=lambda: choose_color(root, ent_back_color))
    label_back_color.grid(row=2, column=0, padx=5, pady=5, sticky="w")
    ent_back_color.grid(row=2, column=1, padx=5, pady=5, sticky="ew")
    button_back_color.grid(row=2, column=2, padx=5, pady=5, sticky="ew")
    entries["backcolor"] = ent_back_color

    #Logoauswahl
    label_logo = tk.Label(root, width=15, text="Auswahl Logo", anchor="w")
    ent_logo = tk.Entry(root)
    button_logo = tk.Button(root, text='Auswahl Logo', command=lambda: filepath(root, ent_logo))
    label_logo.grid(row=3, column=0, padx=5, pady=5, sticky="w")
    ent_logo.grid(row=3, column=1, padx=5, pady=5, sticky="ew")
    button_logo.grid(row=3, column=2, padx=5, pady=5, sticky="ew")
    entries["logo"] = ent_logo

    #Speicherortauswahl
    label_save_dir = tk.Label(root, width=15, text="Speicherort", anchor="w")
    ent_save_dir = tk.Entry(root)
    button_save_dir = tk.Button(root, text='Speicherort', command=lambda: save_dir(root, ent_save_dir))
    label_save_dir.grid(row=4, column=0, padx=5, pady=5, sticky="w")
    ent_save_dir.grid(row=4, column=1, padx=5, pady=5, sticky="ew")
    button_save_dir.grid(row=4, column=2, padx=5, pady=5, sticky="ew")
    entries["save_where"] = ent_save_dir

    # Eingabemaske Dateiname
    label_file_name = tk.Label(root, width=15, text="Dein Dateiname", anchor="w")
    ent_file_name = tk.Entry(root)
    label_file_name.grid(row=5, column=0, padx=5, pady=5, sticky="w")
    ent_file_name.grid(row=5, column=1, padx=5, pady=5, sticky="ew")
    entries["file_name"] = ent_file_name
    
    return entries

def save_qr_code(entries, root):  # Änderung: Funktion hinzugefügt
    url = entries['url'].get()
    save_where = entries['save_where'].get()
    color = entries['color'].get() or "black"
    backcolor = entries['backcolor'].get() or "white"
    logo_name = entries['logo'].get() or "na"
    filename = entries['file_name'].get()
    qr_generator.create_qr_code(url=url, save_where=save_where, color=color, backcolor=backcolor, logo_name=logo_name, filename=filename)
    speichern_correct = tk.Label(root, width=15, text="Gespeichert", anchor="w")
    speichern_correct.grid(row=7, column=0, padx=5, pady=5, sticky="ew")
