import pandas
import datetime as dt
import random
import smtplib

today = dt.datetime.today()
df = pandas.read_csv("birthdays.csv")
df = df[df["month"] == today.month]
df = df[df["day"] == today.day]
birthday_people = df["name"].to_dict()
birthday_emails = df["email"].to_dict()
my_email = ""
password = ""
indices = [key for key in birthday_people]

for i in range(len(df)):
    rng = random.randint(0, 2)
    print(rng)
    email = None
    if rng == 0:
        with open("letter_templates/letter_1.txt") as letter:
            email = letter.read().replace("[NAME]", birthday_people[indices[i]])
    elif rng == 1:
        with open("letter_templates/letter_2.txt") as letter:
            email = letter.read().replace("[NAME]", birthday_people[indices[i]])
    elif rng == 2:
        with open("letter_templates/letter_3.txt") as letter:
            email = letter.read().replace("[NAME]", birthday_people[indices[i]])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=birthday_emails[indices[i]], msg="Subject:Happy Birthday!\n\n" + email)



