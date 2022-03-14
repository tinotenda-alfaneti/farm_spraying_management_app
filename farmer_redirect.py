from tkinter import Label, Entry, Button
from summary_speech import ReadSummary

class Register:
    '''Class for registeration and registration window'''
    
    def __init__(self, window, user, name, welcome_label, notification_message):
        
        # initializing window
        self.window = window
        self.user = user
        self.name  = name
        self.notification_message = notification_message
        self.welcome_label = welcome_label
        self.font_name = "Courier"
        

    def capture_data(self):
        
        '''Function for registration user interface'''

        # register button
        self.register_button = Button(self.window, text="Register", command = self.register_info, font=(self.font_name, 10, "bold"), fg="red", bg="white")
        self.register_button.grid(row=5, column=1, padx=10, pady=10)

        # city name
        self.city_label = Label(self.window, text="Name of City the farm is located: ", fg="red")
        self.city_label.grid(row=1, column=0, pady=5)

        self.city_entry = Entry(self.window, width = 50)
        self.city_entry.grid(row=1, column=1)

        # spraying date
        self.spraying_date_label = Label(self.window, text="Spraying Date (yyyy-mm-dd): ", fg="red")
        self.spraying_date_label.grid(row=2, column=0, pady=5)

        self.spraying_date_entry = Entry(self.window, width = 50)
        self.spraying_date_entry.grid(row=2, column=1)

        # expiry of spray application
        self.spray_expiry_label = Label(self.window, text="What is the number of days of spray expiry: ", fg="red")
        self.spray_expiry_label.grid(row=3, column=0)

        self.spray_expiry_entry = Entry(self.window, width = 10)
        self.spray_expiry_entry.grid(row=3, column=1)

    def register_info(self):
        
        '''function for capturing the information'''

        self.city = self.city_entry.get()
        self.last_spray_date = self.spraying_date_entry.get()
        self.spray_expiry = self.spray_expiry_entry.get()

        if "" not in (self.city, self.last_spray_date, self.spray_expiry): # checking if all fields are filled

            self.farmer_register = open("farmer_record.csv", "w")
            self.farmer_register.write("{},{},{},{}\n".format(self.user, self.city, self.last_spray_date, self.spray_expiry))
            self.farmer_register.close()
            
            # clearing the screen
            self.city_label.destroy()
            self.city_entry.destroy()
            self.spraying_date_label.destroy()
            self.spraying_date_entry.destroy()
            self.spray_expiry_label.destroy()
            self.spray_expiry_entry.destroy()
            self.register_button.destroy()


            self.welcome_label.config(text="Registration Successful, " + self.name)
            self.success_registration()
            
    # successful registration screen
    def success_registration(self):
        
        '''function for the successful registration screen and log in'''
        farmer_details = open("farmer_record.csv", "r")
        for record in farmer_details:
            spray_date = record.split(",")[2]
            expiry = record.split(",")[3]

        analysis_speech = ReadSummary(self.notification_message)
        
        self.welcome_label.config(text=f"NOTIFICATION\n\nYour last spray was on {spray_date}\nExpiring {expiry} days from day of application.")

        self.calculator_button = Button(self.window, text="Update Personal Info", command = '', font=(self.font_name, 10, "bold"), fg="red", bg="white")
        self.calculator_button.grid(row=1, column=0, padx=10, pady=10)

        self.study_button = Button(self.window, text="Read Summary", command = analysis_speech.read_aloud, font=(self.font_name, 10, "bold"), fg="red", bg="white")
        self.study_button.grid(row=1, column=1, padx=10, pady=10)