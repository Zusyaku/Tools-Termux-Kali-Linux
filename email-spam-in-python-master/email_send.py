import smtplib
print('*** Start of the Program ***')
while True:
    sender = "email"
    sender_password = "pass"
    receivers = '@gmail.com'

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender,sender_password )
     
    message_body = "This is test email"
    server.sendmail(sender, receivers, message_body)
    print('email sent')
#server.quit()
