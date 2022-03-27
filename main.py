# for graphical user interface
from math import fabs
from tkinter import Tk, Label, Button, Entry 

# classes

from farmer_redirect import Register
from check_conditions import create_message

# running the function continuously
create_message()


# checking the farmer's records
def check_user(user, pwd):
    
    '''function to check if the user is registered. If not, it takes the farmer to registration'''
    
    # creating an instance of the Register class
    farmer_register = Register(window, user, pwd, welcome_label, create_message())
    
    registered_farmer = open("farmer_record.csv", "r")
    for record in registered_farmer:
        if user == record.split(",")[0].strip() and pwd == record.split(",")[1].strip():
            farmer_register.success_registration()
            return None

    registered_farmer.close()
    # registering the farmer
    farmer_register.capture_data()

# GUI welcome function after log in button
def welcome():
    
    '''Function that welcomes the user'''
    
    user = username.get()  # Taking the input from the entry widget 
    pwd = password.get()
    
    # checking if the entry box is not empty
    if user != "":
        username_label.destroy()
        welcome_label.config(text="Hello, Farmer " + user)
        username.destroy()
        welcome_label.grid(row=0, column=0, columnspan=3)
        login_button.destroy()
        password_label.destroy()
        password.destroy()
        check_user(user, pwd)


# ------------- Graphical User Interface ------------------

 # initialising the graphical user interface window 
window = Tk()
# screen title
window.title("Spraying Management App")
window.config(padx=100, pady=100, background="lightgreen")

# font
font_name = "Courier"

welcome_label = Label(window, text="Welcome to Spraying Management App", font=(font_name, 20, "bold"), fg="red", bg="white")
welcome_label.grid(row=0, column=0, columnspan=3, pady=20)


username_label = Label(window, text="Enter Username: ", fg="red")
username_label.grid(row=1, column=0)

username = Entry(window, width = 50)
username.grid(row=1, column=1)

password_label = Label(window, text="Enter Password: ", fg="red")
password_label.grid(row=2, column=0)

password = Entry(window, width = 50)
password.grid(row=2, column=1)

login_button = Button(window, text="Log in", command = welcome, font=(font_name, 10, "bold"), fg="red", bg="white")
login_button.grid(row=3, column=1, padx=10, pady=10)


window.mainloop()



