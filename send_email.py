#!/usr/bin/python3

import smtplib
from email.mime.text import MIMEText


def send_email(to, gmail_user, gmail_password, subject, body):
    # Change to your own account information
    to = to
    gmail_user = gmail_user
    gmail_password = gmail_password
    smtpserver = smtplib.SMTP('smtp.gmail.com', 587)
    smtpserver.ehlo()
    smtpserver.starttls()
    #smtpserver.ehlo()
    smtpserver.login(gmail_user, gmail_password)

    # craft the email
    mail_body = body
    msg = MIMEText(mail_body)
    msg['Subject'] = subject
    msg['From'] = gmail_user
    msg['To'] = to

    # and send the mail
    smtpserver.sendmail(gmail_user, [to], msg.as_string())
    smtpserver.quit()
