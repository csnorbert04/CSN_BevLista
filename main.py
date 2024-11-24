##main
import tkinter as tk
from tkinter import messagebox
from main_modul import BevasarloLista

def main():
    lista = BevasarloLista()

    def hozzaad_elem():
        elem = beviteli_mezo.get().strip()
        if lista.hozzaad(elem):
            frissit_lista()
            beviteli_mezo.delete(0, tk.END)
        else:
            messagebox.showwarning("Figyelmeztetés", f"'{elem}' már a listában van, vagy üres!")

    def torol_elem():
        elem = beviteli_mezo.get().strip()
        if lista.torol(elem):
            frissit_lista()
            beviteli_mezo.delete(0, tk.END)
        else:
            messagebox.showwarning("Figyelmeztetés", f"'{elem}' nincs a listában!")

    def random_hozzaad():
        random_elem = lista.random_elem()
        if lista.hozzaad(random_elem):
            frissit_lista()
        else:
            messagebox.showinfo("Info", f"A '{random_elem}' már a listában van.")

    def frissit_lista():
        lista_mezo.delete(0, tk.END)
        for elem in lista.listaz():
            lista_mezo.insert(tk.END, elem)

    # GUI ablak
    ablak = tk.Tk()
    ablak.title("Bevásárlólista")

    # Beviteli mező éss gombok
    tk.Label(ablak, text="Adj hozzá elemet a listához:").pack()
    beviteli_mezo = tk.Entry(ablak)
    beviteli_mezo.pack()

    hozzaad_gomb = tk.Button(ablak, text="Hozzáad", command=hozzaad_elem)
    hozzaad_gomb.pack()

    torol_gomb = tk.Button(ablak, text="Töröl", command=torol_elem)
    torol_gomb.pack()

    random_gomb = tk.Button(ablak, text="Random elem hozzáad", command=random_hozzaad)
    random_gomb.pack()

    # megjelenítés
    tk.Label(ablak, text="Bevásarlólista:").pack()
    lista_mezo = tk.Listbox(ablak, width=40, height=10)
    lista_mezo.pack()


    ablak.mainloop()

if __name__ == "__main__":
    main()
