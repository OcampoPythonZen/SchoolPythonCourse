from tkinter import Tk, Button, Frame, StringVar, Entry
import random
import string

class PasswordGenerator(Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.characters = list(string.ascii_letters + string.punctuation)
        self.password = None
        self.len= 16
        self.pack()
        self.btnPassword()
        self.txtPassword()
        self.btnExit()

    def _newPassword(self):
        self.password = ''.join(random.choices(self.characters, k=self.len))
        self.sv_txtPassword.set(self.password)
        print(self.password)

    def btnPassword(self):
        self._btnPassword = Button(self)
        self._btnPassword['text'] = 'New Password'
        self._btnPassword['command'] = self._newPassword
        self._btnPassword.pack(side='left')

    def txtPassword(self):
        self.sv_txtPassword = StringVar(self)
        self._txtPassword = Entry(self, textvariable=self.sv_txtPassword) 
        self._txtPassword['width'] = 32
        self._txtPassword.pack(side="left")

    def btnExit(self):
        self._btnExit = Button(self)
        self._btnExit['text']='Close'
        self._btnExit['fg']='red'
        self._btnExit['command']=self.master.destroy
        self._btnExit.pack(side='right')

if __name__ == '__main__':
    root = Tk()
    root.title('Password Generator by Ed.')
    app = PasswordGenerator(master=root)
    app.mainloop()
    
