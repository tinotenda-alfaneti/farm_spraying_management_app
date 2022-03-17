
from weather import Weather
from email_notifier import EmailSender
from whatsapp_notifier import WhatsappMessageSender
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
