from tkinter import Tk, Button, Frame, StringVar, Entry
import random
import string

class PasswordGenerator(Frame):

    def __init__(self, master) -> None:
        self.master = master
        self.master.geometry("200X200")
        self.characters = list(string.ascii_letters + string.punctuation)
        self.password = None
        self.width= 8
        self.pack()
        self.btnPassword()
        self.txtPassword()
        self.btnExit()

    def _nuevoPassword(self):
        pass

    def btnPassword(self):
        self._btnPassword = Button(self)
        self._btnPassword['text'] = 'New Password'
        self._btnPassword['command'] = self._nuevoPassword
        self._btnPassword.pack(side='left')

    def txtPassword(self):
        self.sv_txtPassword = StringVar(self)
        self._txtPassword = Entry(self, textvariable=self.sv_txtPassword) 
        self._txtPassword['width'] = 32
        self._txtPassword.pack(side="left")
