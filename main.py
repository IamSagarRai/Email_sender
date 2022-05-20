import smtplib
import ssl
from email.message import EmailMessage


subject = "Sending an anonymous test email!"
body = "Vs code is cool simulation of figurative things and Idont know what"
sender_email = ""  # Enter your email address
receiver_email = ""  # Enter receiver email address
password = input("Enter a password: ")

message = EmailMessage()
message["From"] = "sender_email" --> Has to be given by the user his/herself !
message["To"] = "receiver_email" --> Has to be given by the user his/herself !
message["Subject"] = "subject" --> Has to be given by the user his/herself !


context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())

print("Officially Sent the email!")
