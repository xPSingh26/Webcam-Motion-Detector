import smtplib
import os
from email.message import EmailMessage
import imghdr

USER = "p.singhx26@gmail.com"
RECEIVER = "p.singhx26@gmail.com"
PASSWORD = os.getenv("PASSWORD")


def send_email(image_path):
    email = EmailMessage()
    email["Subject"] = "New client alert!"
    email.set_content("A new customer has been detected!")

    with open(image_path, 'rb') as file:
        content = file.read()

    email.add_attachment(content, maintype="image", subtype=imghdr.what(None, content))

    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(USER, PASSWORD)
    gmail.sendmail(USER, RECEIVER, email.as_string())
    gmail.quit()


if __name__ == "__main__":
    send_email("images/94.png")
