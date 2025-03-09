import getpass
import smtplib

with smtplib.SMTP('smtp.gmail.com', 587) as smtp_obj:
    smtp_obj.ehlo()
    smtp_obj.starttls()

    email = getpass.getpass("Email: ")
    password = getpass.getpass("Password: ")
    smtp_obj.login(email, password)

    from_address = email
    to_address = email
    subject = input("Enter the subject line: ")
    message = input("Type out the message you want to send: ")
    send_message = "Subject: " + subject + '\n' + message
    smtp_obj.sendmail(from_address, to_address, send_message)
