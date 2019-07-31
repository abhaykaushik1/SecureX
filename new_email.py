import smtplib

import config


def send_email(subject: str, name: str):
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(config.EMAIL_ADDRESS, config.PASSWORD)
        message = "Subject: {}\n\n{}".format(subject, config.message(name))
        server.sendmail(config.EMAIL_ADDRESS, config.EMAIL_ADDRESS, message)
        server.quit()
        print("Success: Email sent!")
    except:
        print("Email failed to send.")


send_email('Login Detected', 'Abhay Kaushik')
