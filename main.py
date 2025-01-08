import tkinter as tk
import inputs


root = tk.Tk()
ents = inputs.makeform(root)
button_speichern = tk.Button(root, text='Speichern', command=lambda: inputs.save_qr_code(ents, root))
button_speichern.grid(row=6, column=0, padx=5, pady=5, sticky="ew")
button_beenden = tk.Button(root, text='Beenden', command=root.quit)
button_beenden.grid(row=6, column=1, padx=5, pady=5, sticky="ew")


root.mainloop()