import smtplib
import random
from datetime import datetime

MY_EMAIL = "maciborek.grzegorz@gmail.com"
PASSWORD = "fpqzkfitelpeacjo"

# connection = smtplib.SMTP("smtp.gmail.com", port=587)
# connection.starttls()
# connection.login(user=MY_EMAIL, password=PASSWORD)
# connection.sendmail(from_addr=MY_EMAIL, to_addrs='gmakuss@gmail.com', msg="Subject:elo mordo!\n\n dziaaa!")
# connection.close()

dt = datetime.now()
name = dt.strftime('%A')
weekday = dt.weekday()

if weekday == 4:
    with open("quotes.txt", "r") as file:
        read_content = file.readlines()
        quote = random.choice(read_content)

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs='gmakuss@gmail.com',
            msg=f"Subject:{name} MOTIVATION\n\n {quote}"
        )
