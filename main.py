import smtplib
# please note go to https://myaccount.google.com/lessecureapps and
# turn it off to allow gmail to send
s = smtplib.SMTP("smtp.gmail.com")
sender_email_id = "gideondaniels.dragoonix@gmail.com"
receiver_email_id = "gideondaniels.dragoonix@gmail.com"
password = input("Enter senders email password")
# starts TLS for security
s.starttls()
# Authentication
s.login(sender_email_id, password)
# message to be sent
message = "Hi guys how are you. I am doing fine\n"
message = message + "How was your task yesterday"
# sending the mail
s.sendmail(sender_email_id, receiver_email_id, message)
# terminating the session
s.quit()
