import smtplib
import ssl
from email.message import EmailMessage


subject = "Sending an anonymous test email!"
body = "Vs code is cool simulation of figurative things and Idont know what"
sender_email = ""  # Enter your email address
receiver_email = ""  # Enter receiver email address
password = input("Enter a password: ")

message = EmailMessage()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject


context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())

print("Officially Send the email!")
