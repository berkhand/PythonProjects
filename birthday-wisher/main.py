##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.


import pandas
import smtplib
import datetime as dt
import random
import os


df = pandas.read_csv("birthdays.csv")
birthdays = df.to_dict(orient="records")

now = dt.datetime.now()


def send_birthday_mail(name, mail):
    letter_list = os.listdir("letter_templates")
    letter_name = random.choice(letter_list)

    with open("letter_templates/" + letter_name) as letter:
        message = letter.read()
        message_new = message.replace("[NAME]", name)

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        my_email = "berqoed@gmail.com"
        my_password = "kxvlvadkumflmzyo"
        subject = "Happy birthday"
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email, to_addrs=mail, msg=f"Subject:{subject}\n\n{message_new}")


for record in birthdays:
    if now.month == record["month"] and now.day == record["day"]:
        send_birthday_mail(record["name"], record["email"])
