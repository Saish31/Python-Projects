from datetime import datetime
import pandas
import random
import smtplib

my_email="saishsail1@gmail.com"
password="*************"
today=(datetime.now().month,datetime.now().day)
data=pandas.read_csv("events.csv")
events_dict = {(data_row["month"], data_row["day"]):data_row for (index, data_row) in data.iterrows()}


def sender(file_path):
    with open(file_path) as letter_file:
        contents=letter_file.read()
        contents=contents.replace("[NAME]",event_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email,password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=event_person["email"],
            msg=f"Subject:Tech Fest Event Reminder\n\n{contents}"
        )


if today in events_dict:
    event_person=events_dict[today]
    if event_person["event"]=="coding":
        file_path = f"letter_templates/letter_1.txt"
        sender(file_path)
    if event_person["event"]=="robot":
        file_path = f"letter_templates/letter_2.txt"
        sender(file_path)
    if event_person["event"]=="conference":
        file_path = f"letter_templates/letter_3.txt"
        sender(file_path)


