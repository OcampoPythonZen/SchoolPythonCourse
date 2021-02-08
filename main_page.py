from tkinter import Frame, Tk, Label, Button


class MyFirstGUI:

    def __init__(self, master):
        self.master = master
        self.master.geometry("500x400")

        self.label = Label(master, text="This is our first GUI!")
        self.label.pack()

        self.greet_button = Button(master, text="Greet", command=self.greet)
        self.greet_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

        self.frame = Frame(bg="lightblue", width=500, height=200)
        self.frame.pack()

        self.frame2 = Frame(bg="yellow", width=500, height=200)
        self.frame2.pack()

    def greet(self):
        print("Greetings!")


if __name__ == "__main__":
    root = Tk(className='Our Main Page...')
    my_gui = MyFirstGUI(root)
    root.mainloop()
