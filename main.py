# for graphical user interface
from tkinter import Tk, Label, Button, Entry 

# classes
from weather import Weather
from email_notifier import EmailSender
from whatsapp_notifier import WhatsappMessageSender
from farmer_redirect import Register
import datetime as dt


def create_message():

    ''' function to create spraying summary'''
    # try-block to catch erro when the file is empty
    try:
        notification_message = "Welcome to Spray Helper Summary\n\n"

        # getting the data from the file
        farmer_summary = open("farmer_record.csv", "r")
        for record in farmer_summary:
            city = record.split(",")[1]
            date_ = record.split(",")[2]
            expiry = record.split(",")[3]

        weather = Weather(city)

        spray_date_list = date_.split("-")
        spray_expiry = int(expiry)
    except:
        return "There is no summary at the moment."

    else:

        spray_date = dt.date(int(spray_date_list[0]), int(spray_date_list[1]), int(spray_date_list[2]))
        next_spray_date = spray_date + dt.timedelta(days=spray_expiry)

        # game conditions
        if dt.date.today() == next_spray_date - dt.timedelta(days=3):
            days_available = [0, 1, 2]
            successful = list()
            for day in days_available:

                date, wind_speed, temperature, humidity, chance_of_rain = weather.day_weather_forecast(day)

                if 2.0 <= wind_speed <= 15.0 and temperature > 25.0 and humidity < 40 and chance_of_rain < 95:
                    successful.append(day)
                elif 2.0 <= wind_speed <= 15.0 and temperature > 25.0 and humidity < 40:
                    if len(successful) == 0:
                        successful.append(day)
                elif 2.0 <= wind_speed <= 15.0 and temperature > 25.0:
                    if len(successful) == 0:
                        successful.append(day)
                elif 2.0 <= wind_speed <= 15.0 or temperature > 25.0 and humidity < 40:
                    if len(successful) == 0:
                        successful.append(day)
            
            if len(successful) == 0:
                notification_message += 'There is high risk of wastage and inefficiency if you spray in the next three days.\nYou have to extend the spraying day.'
            else:
                notification_message += "The most successful day for spraying is ", weather.day_weather_forecast(max(successful))[0]


            # sending whatsapp_notification
            analysis_summary = WhatsappMessageSender(notification_message)
            analysis_summary.send_message()

            # sending email notification
            analysis_email = EmailSender(notification_message)
            analysis_email.send_email()
        return notification_message

# running the function continuously
create_message()


# checking the farmer's records
def check_user(user, name):
    
    '''function to check if the user is registered. If not, it takes the farmer to registration'''
    
    # creating an instance of the Register class
    farmer_register = Register(window, user, name, welcome_label, create_message())
    
    registered_farmer = open("farmer_record.csv", "r")
    for record in registered_farmer:
        if user == record.split(",")[0].strip():
            farmer_register.success_registration()
            return None

    registered_farmer.close()
    # registering the farmer
    farmer_register.capture_data()

# GUI welcome function after log in button
def welcome():
    
    '''Function that welcomes the user'''
    
    user = username.get()  # Taking the input from the entry widget 
    name = user.split("@")[0]
    
    # checking if the entry box is not empty
    if user != "":
        username_label.destroy()
        welcome_label.config(text="Hello, Farmer " + name)
        username.destroy()
        welcome_label.grid(row=0, column=0, columnspan=2)
        login_button.destroy()
        check_user(user, name)


# ------------- Graphical User Interface ------------------

 # initialising the graphical user interface window 
window = Tk()
# screen title
window.title("Spraying Management App")
window.config(padx=100, pady=100, background="lightgreen")

# font
font_name = "Courier"

welcome_label = Label(window, text="Welcome to Spraying Management App", font=(font_name, 20, "bold"), fg="red", bg="white")
welcome_label.grid(row=0, column=0, columnspan=2, pady=20)


username_label = Label(window, text="Enter Username(Name@NationalID, e.g. Joe@1234): ", fg="red")
username_label.grid(row=1, column=0)

username = Entry(window, width = 50)
username.grid(row=1, column=1)

login_button = Button(window, text="Log in", command = welcome, font=(font_name, 10, "bold"), fg="red", bg="white")
login_button.grid(row=2, column=1, padx=10, pady=10)


window.mainloop()



