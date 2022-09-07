import tkinter as tk

from models.materiaal import Materiaal

class App(tk.Frame):

    def __init__(self, master=None):

        w = tk.Label(master, text="Materiaal", font=("Arial", 25))
        w.grid(row = 1, column = 1, columnspan = 2)

        w = tk.Label(master, text="Naam")
        w.grid(row = 2, column = 1)

        self.naam = tk.StringVar()
        w = tk.Entry(master, textvariable=self.naam)
        w.grid(row = 2, column = 2)

        w = tk.Label(master, text="Omschrijving")
        w.grid(row = 3, column = 1)

        self.omschrijving = tk.StringVar()
        w = tk.Entry(master, textvariable=self.omschrijving)
        w.grid(row = 3, column = 2)

        w = tk.Label(master, text="Atacode")
        w.grid(row = 4, column = 1)

        self.atacode = tk.StringVar()
        w = tk.Entry(master, textvariable=self.atacode)
        w.grid(row = 4, column = 2)

        w = tk.Label(master, text="Type")
        w.grid(row = 5, column = 1)

        self.type = tk.StringVar()
        w = tk.Entry(master, textvariable=self.type)
        w.grid(row = 5, column = 2)

        w = tk.Label(master, text="Partnummer")
        w.grid(row = 6, column = 1)

        self.partnummer = tk.StringVar()
        w = tk.Entry(master, textvariable=self.partnummer)
        w.grid(row = 6, column = 2)

        w = tk.Label(master, text="Serienummer")
        w.grid(row = 7, column = 1)

        self.serienummer = tk.StringVar()
        w = tk.Entry(master, textvariable=self.serienummer)
        w.grid(row = 7, column = 2)

        w = tk.Label(master, text="Positie")
        w.grid(row = 8, column = 1)

        self.positie = tk.StringVar()
        w = tk.Entry(master, textvariable=self.positie)
        w.grid(row = 8, column = 2)

        w = tk.Button(master, text="Opslaan", command=self.click_handler)
        w.grid(row = 9, column = 1, columnspan = 2)


    def click_handler(self):
        materiaal = Materiaal(
            self.naam,
            self.omschrijving,
            self.atacode,
            self.type,
            self.partnummer,
            self.serienummer,
            self.positie)
        pass


if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('300x500+100+100')  # width x height + x_offset + y_offset
    root.title('Materiaal')
    app = App(root)
    root.mainloop()