import tkinter as tk

from models.materiaal import Materiaal
from models.equipment import Equipment

class App(tk.Frame):

    def __init__(self, master=None):

        self.list = ['een','twee','drie']

        w = tk.Label(master, text="Equipment", font=("Arial", 25))
        w.pack()

        list_var = tk.StringVar(value = self.list)
        w = tk.Listbox(master, listvariable = list_var)
        w.pack()



if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('300x500+100+100')  # width x height + x_offset + y_offset
    root.title('Equipment')
    app = App(root)
    root.mainloop()