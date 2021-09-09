import tkinter as tk

class Calc(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Calculator')
        self.header = tk.Label(self, text='Tkinter Calculator', foreground='blue')
        self.header.pack(padx=0)

        #Preview Zone of the Calculator

        #Number buttons
        self.one = tk.Button(self, text="1", border='green').grid(column=0, row=0)
        self.two = tk.Button(self, text="2", border='green').grid(column=0, row=0)
        self.three = tk.Button(self, text="3", border='green').grid(column=0, row=0)
        self.four = tk.Button(self, text="4", border='green').grid(column=0, row=0)
        self.five = tk.Button(self, text="5", border='green').grid(column=0, row=0)
        self.six = tk.Button(self, text="6", border='green').grid(column=0, row=0)
        self.seven = tk.Button(self, text="7", border='green').grid(column=0, row=0)
        self.eight = tk.Button(self, text="8", border='green').grid(column=0, row=0)
        self.nine = tk.Button(self, text="9", border='green').grid(column=0, row=0)
        self.zero = tk.Button(self, text="0", border='green').grid(column=0, row=0)

        #function buttons
        self.add = tk.Button(self, text="+", border='green').grid(column=0, row=0)
        self.sub = tk.Button(self, text="-", border='green').grid(column=0, row=0)
        self.mpy = tk.Button(self, text="x", border='green').grid(column=0, row=0)
        self.dvd = tk.Button(self, text="/", border='green').grid(column=0, row=0)
        self.fact = tk.Button(self, text="!", border='green').grid(column=0, row=0)
        self.eqls = tk.Button(self, text="=", border='green').grid(column=0, row=0)
        self.sqrt = tk.Button(self, text="Sqr root", border='green').grid(column=0, row=0)
        self.ee = tk.Button(self, text="e", border='green').grid(column=0, row=0)
        self.ii = tk.Button(self, text="i", border='green').grid(column=0, row=0)

        #footer Label
        self.footer = tk.Label(self, text='Made by Joseph Gakah......Property of Roentgen Industries', foreground='blue')
        self.footer.pack(padx=0)


if __name__ == "__main__":
    Calc = Calc()
    Calc.mainloop()