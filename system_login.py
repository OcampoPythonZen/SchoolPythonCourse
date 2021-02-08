from tkinter import Button, Entry, Label, Label, Tk, Toplevel
from class_main_page import MainPage

window = Tk(className='Login System')

# set window size
window.geometry("500x400")
# 500 width and 400 height

# Label to show the username
str = 'Please, Type your username:'
username = Label(window, text=str)
username.grid(pady=5, row=0, column=0)

# Entry for the username == input()
username_entry = Entry(window)
username_entry.grid(pady=5, row=0, column=1)

password = Label(window, text="Please, Type your password")
password.grid(pady=5, row=1, column=0)
pass_entry = Entry(window)
pass_entry.grid(pady=5, row=1, column=1)


def validate_user():
    # Validate if user and password are the same
    if username_entry.get() == 'user' and pass_entry.get() == 'pass':
        # Make the done LAbel when credentials are correct
        done = Label(window, text="ACCESING!.", fg='green')
        done.grid(row=2, column=2)
    else:
        # Define a Label Widget WRONG
        wrong = Label(window, text="ACCESS DENIED!.", fg='red')
        wrong.grid(row=3, column=2)


sumbit = Button(window, bg='green', text='Submit',
                command=validate_user, width=50)
sumbit.grid(padx=10, pady=10, row=2, column=0, columnspan=2)


window.mainloop()
