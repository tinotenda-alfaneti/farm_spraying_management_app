from weather import Weather
from email_notifier import EmailSender
from whatsapp_notifier import WhatsappMessageSender
from summary_speech import ReadSummary
import datetime as dt

notification_message = "Welcome to Atarist Spraying Helper.\n\n"

'''
def get_info():
    town_name = input("Enter the name of your town: ").title()
    spray_date_list = input("Enter the date of last spray application (yyyy-mm-dd): ").split("-")
    spray_expiry = input("What is the number of days of spray expiry: ")

    return town_name, spray_date, spray_expiry
'''

weather = Weather("Accra")

spray_date_list = ["2022", "03", "02"]
spray_expiry = 8

spray_date = dt.date(int(spray_date_list[0]), int(spray_date_list[1]), int(spray_date_list[2]))
next_spray_date = spray_date + dt.timedelta(days=spray_expiry)


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

    # summary speech
    analysis_speech = ReadSummary(notification_message)
    analysis_speech.read_aloud()

    # sending email notification
    analysis_email = EmailSender(notification_message)
    analysis_email.send_email()




