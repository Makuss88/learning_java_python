import smtplib
import time

import requests
from datetime import datetime

MY_EMAIL = "maciborek.grzegorz@gmail.com"
MY_PASS = "fpqzkfitelpeacjo"
MY_LAT = 50.038631
MY_LONG = 19.222530


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True


while True:
    if is_iss_overhead() and is_night():
        print('ok')
        connection = smtplib.SMTP("smtp.gmail.com", port=587)
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASS)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs='gmakuss@gmail.com', msg="Subject:elo mordo!\n\n dziaaa!")
        connection.close()
    time.sleep(60)
#
# # If the ISS is close to my current position,
# # and it is currently dark
# # Then email me to tell me to look up.
# # BONUS: run the code every 60 seconds.
