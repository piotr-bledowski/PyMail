import smtplib
import ssl

from config import *
from credentials import *

simple_email_context = ssl.create_default_context()
recipient = EMAIL_ADDRESS
message = 'Hello!'

try:
    print('Connecting to server...')
    # Create a connection with smtplib
    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.starttls(context=simple_email_context)
    server.login(EMAIL_ADDRESS, PASSWORD)
    print('Connection established!')
    print(f'Sending email to {recipient}')
    server.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, message)
    print('Email successfully sent!')
except Exception as e:
    print(e)
finally:
    server.quit() # Close the thing once done
