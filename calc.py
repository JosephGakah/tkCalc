import tkinter as tk

class Calc(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Calculator')
        self.header = tk.Label(self, text='Tkinter Calculator', foreground='blue')
        self.header.grid()

        #navigation keys

        #Calculator Display
        self.display = tk.Entry(self)
        #self.display.grid(column=0,row=0)

        #Number buttons
        self.one = tk.Button(self, text="1").grid(column=0, row=0)
        self.two = tk.Button(self, text="2").grid(column=0, row=0)
        self.three = tk.Button(self, text="3").grid(column=0, row=0)
        self.four = tk.Button(self, text="4").grid(column=0, row=0)
        self.five = tk.Button(self, text="5").grid(column=0, row=0)
        self.six = tk.Button(self, text="6").grid(column=0, row=0)
        self.seven = tk.Button(self, text="7").grid(column=0, row=0)
        self.eight = tk.Button(self, text="8").grid(column=0, row=0)
        self.nine = tk.Button(self, text="9").grid(column=0, row=0)
        self.zero = tk.Button(self, text="0").grid(column=0, row=0)

        #function buttons
        self.add = tk.Button(self, text="+").grid(column=0, row=0)
        self.sub = tk.Button(self, text="-").grid(column=0, row=0)
        self.mpy = tk.Button(self, text="x").grid(column=0, row=0)
        self.dvd = tk.Button(self, text="/").grid(column=0, row=0)
        self.fact = tk.Button(self, text="!").grid(column=0, row=0)
        self.eqls = tk.Button(self, text="=").grid(column=0, row=0)
        self.sqrt = tk.Button(self, text="Sqr root").grid(column=0, row=0)
        self.ee = tk.Button(self, text="e").grid(column=0, row=0)
        self.ii = tk.Button(self, text="i").grid(column=0, row=0)

        #footer Label
        self.footer = tk.Label(self, text='Made by Joseph Gakah......Property of Roentgen Industries', foreground='blue')
        self.footer.grid(column=0,row=0)


if __name__ == "__main__":
    Calc = Calc()
    Calc.mainloop()