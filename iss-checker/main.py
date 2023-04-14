import requests
from datetime import datetime
import math
import smtplib
from threading import Timer

MY_LAT = 51.435977
MY_LONG = 5.417767


def am_i_close_to_iss():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")

    response.raise_for_status()

    data = response.json()

    iss_long = float(data["iss_position"]["longitude"])
    iss_lat = float(data["iss_position"]["latitude"])

    pos = (iss_lat, iss_long)
    lat_diff = math.fabs(MY_LAT - iss_lat)
    long_diff = math.fabs(MY_LONG - iss_long)

    res = lat_diff < 5 and long_diff < 5
    print(f"Am I close to ISS: {res}")
    return res


def is_it_evening():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)

    response.raise_for_status()

    data = response.json()

    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    now = datetime.now().hour

    res = now >= sunset or now <= sunrise
    print(f"is it evening: {res}")

    return res


def send_mail():
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        my_email = "berqoed@gmail.com"
        mail = "berkhand@gmail.com"
        my_password = "kxvlvadkumflmzyo"
        subject = "ISS is close to home"
        message_new = "Check the sky"
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email, to_addrs=mail, msg=f"Subject:{subject}\n\n{message_new}")


def check():
    if is_it_evening() and am_i_close_to_iss():
        send_mail()
    t = Timer(60, check)
    t.start()


check()







