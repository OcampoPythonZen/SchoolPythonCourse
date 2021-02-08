from tkinter import Frame, Tk, Label, Button, mainloop

class MainPage:

    def __init__(self, master):
        self.master = master
        self.master.geometry("500x400")

        self.label = Label(master, text='This is our first class GUI')
        self.label.pack()

        self.greet_button = Button(master, text='Greet.!', command=self.greet)
        self.greet_button.pack()

        self.close_button = Button(master, text='Closing, Bye-Bye.', command=master.quit)
        self.close_button.pack()

        self.frame_one = Frame(master, bg='lightblue', width=500, height=100)
        self.frame_one.pack()

        self.frame_two = Frame(master, bg='yellow', width=500, height=100)
        self.frame_two.pack()

    def greet(self):
        print("Greetings.!")

if __name__ == '__main__':
    master = Tk(className='Main Page with classes.')
    my_gui = MainPage(master)
    master.mainloop()
