import tkinter as tk
import tkinter.messagebox

class App(tk.Frame):

    def __init__(self, master=None):
        self.teller = 0

        w = tk.Label(master, text="Materiaal")
        w.grid(row = 1, column = 1, columnspan = 2)

        w = tk.Label(master, text="Naam")
        w.grid(row = 2, column = 1)

        self.text1 = tk.StringVar()
        w = tk.Entry(master, textvariable=self.text1)
        w.grid(row = 2, column = 2)



        w = tk.Label(master, text="Omschrijving")
        w.grid(row = 3, column = 1)

        self.text2 = tk.StringVar()
        w = tk.Entry(master, textvariable=self.text2)
        w.grid(row = 3, column = 2)


        w = tk.Label(master, text="Atacode")
        w.grid(row = 4, column = 1)

        self.text2 = tk.StringVar()
        w = tk.Entry(master, textvariable=self.text2)
        w.grid(row = 4, column = 2)


        w = tk.Label(master, text="Type")
        w.grid(row = 5, column = 1)

        self.text2 = tk.StringVar()
        w = tk.Entry(master, textvariable=self.text2)
        w.grid(row = 5, column = 2)


        w = tk.Label(master, text="Partnummer")
        w.grid(row = 6, column = 1)

        self.text2 = tk.StringVar()
        w = tk.Entry(master, textvariable=self.text2)
        w.grid(row = 6, column = 2)

        w = tk.Label(master, text="Serienummer")
        w.grid(row = 7, column = 1)

        self.text2 = tk.StringVar()
        w = tk.Entry(master, textvariable=self.text2)
        w.grid(row = 7, column = 2)

        w = tk.Label(master, text="Positie")
        w.grid(row = 8, column = 1)

        self.text2 = tk.StringVar()
        w = tk.Entry(master, textvariable=self.text2)
        w.grid(row = 8, column = 2)

        w = tk.Button(master, text="Opslaan", command=self.click_handler)
        w.grid(row = 9, column = 1, columnspan = 2)


    def click_handler(self):
        pass


if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('300x500+100+100')  # width x height + x_offset + y_offset
    root.title('Materiaal')
    app = App(root)
    root.mainloop()