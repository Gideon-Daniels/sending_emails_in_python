# building simple messages with subject

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

send_email_id = "gideon.daniels@yahoo.com"
receiver_email_id = "rmazenge@gmail.com"
password = input("Enter your password")
subject = "Greetings"
msg = MIMEMultipart()
msg['From'] = send_email_id
msg['To'] = subject
body = "Hi guys how are you. I am doing fine\n"
body = body + "how was your task yesterday"
msg.attach(MIMEText(body, 'plain'))
text = msg.as_string()
s = smtplib.SMTP("smtp.gmail.com", 587)
# start TLS for security
s.starttls()
# Authentication
s.login(send_email_id, password)
# start TLS for security
s.starttls()
s.login(send_email_id, password)
# message to be send

# sending the mail
s.sendmail(send_email_id, receiver_email_id, text)
# terminating the session
s.quit()
