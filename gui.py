import tkinter as tk
import time, main, logger, download


def open():
    window = tk.Tk(className="Teste")

    greeting = tk.Label(text="Insira o Link do Vídeo/Playlist:")
    greeting.pack()

    global list
    list = tk.Listbox(height=2, selectmode="SINGLE")
    list.insert(1, "mp3")
    list.insert(2, "mp4")
    list.pack()

    global entLink
    entLink = tk.Entry(master=window, width=50)
    entLink.pack()

    btnLink = tk.Button(master=window, text="Baixar !", command=baixarBtn)
    btnLink.pack()

    window.mainloop()

def baixarBtn():
    if not list.curselection():
        return
    start = time.time()
    download.manager(entLink.get(), list.get(list.curselection()))
    end = time.time()
    logger.debug(f"Finalizado em: {end - start}")