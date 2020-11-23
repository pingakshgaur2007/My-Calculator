from tkinter import *


class my_window:
    def __init__(self, window):
        '''
        Creating our variables for our window
        '''
        # Creating our Labels to display our text on screen
        self.label1 = Label(window, text="My Calculator",font="freesansbold 32")
        self.label2 = Label(window, text="First Number",font="freesansbold 16")
        self.label3 = Label(window, text="Second Number",font="freesansbold 16")
        self.label4 = Label(window, text="Result", font="freesansbold 16")

        # Creating our Entries to type and see the result
        self.entry1 = Entry(bd=2, font="16")
        self.entry2 = Entry(bd=2, font="16")
        self.entry3 = Entry(bd=2, font="16")

        # Creating our Buttons for our window's functionality
        self.button1 = Button(
            window, text="+", font="freesansbold 16", command=self.add)
        self.button2 = Button(window, text="-", font="freesansbold 16")
        self.button3 = Button(
            window, text="x", font="freesansbold 16", command=self.muiltiply)
        self.button4 = Button(
            window, text="/", font="freesansbold 16", command=self.divide)
        self.button5 = Button(
            window, text="^2", font="freesansbold 16", command=self.power)

        self.button2.bind('<Button-1>', self.subtract)

        '''
        Placing our variables on our screen
        '''
        # Placing our Labels on our screen
        self.label1.place(x=270, y=80)
        self.label2.place(x=150, y=180)
        self.label3.place(x=150, y=230)
        self.label4.place(x=150, y=420)

        # Placing our Entries on our screen
        self.entry1.place(x=305, y=180)
        self.entry2.place(x=305, y=230)
        self.entry3.place(x=305, y=420)

        # Placing our Buttons on our screen
        self.button1.place(x=220, y=320)
        self.button2.place(x=280, y=320)
        self.button3.place(x=340, y=320)
        self.button4.place(x=400, y=320)
        self.button5.place(x=460, y=320)

    def add(self):
        self.entry3.delete(0, 'end')
        number1 = float(self.entry1.get())
        number2 = float(self.entry2.get())
        result = number1 + number2
        self.entry3.insert(END, str(result))

    def subtract(self, event):
        self.entry3.delete(0, 'end')
        number1 = float(self.entry1.get())
        number2 = float(self.entry2.get())
        result = number1 - number2
        self.entry3.insert(END, str(result))

    def muiltiply(self):
        self.entry3.delete(0, 'end')
        number1 = float(self.entry1.get())
        number2 = float(self.entry2.get())
        result = number1 * number2
        self.entry3.insert(END, str(result))

    def divide(self):
        self.entry3.delete(0, 'end')
        number1 = float(self.entry1.get())
        number2 = float(self.entry2.get())
        result = number1 / number2
        self.entry3.insert(END, str(result))

    def power(self):
        self.entry3.delete(0, 'end')
        number1 = float(self.entry1.get())
        number2 = float(self.entry2.get())
        result = number1 ** number2
        self.entry3.insert(END, str(result))


window = Tk()

my_win = my_window(window)

window.title("My Calculator")
window.geometry("800x600")
window.mainloop()
