import tkinter as tk

from models.materiaal import Materiaal
from models.equipment import Equipment

class App(tk.Frame):

    def __init__(self, master=None):

        w = tk.Label(master, text="Equipment", font=("Arial", 25))
        w.grid(row = 1, column = 1, columnspan = 2)

        self.list = tk.StringVar()
        w = tk.Listbox(self, listvariable = self.list)



if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('300x500+100+100')  # width x height + x_offset + y_offset
    root.title('Equipment')
    app = App(root)
    root.mainloop()