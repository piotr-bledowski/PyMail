import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

from config import *
from credentials import *

#simple_email_context = ssl.create_default_context()
message = 'Hello!'
subject = 'Multi-recipient attachment test'

def send_email():
    for recipient in RECIPIENTS:
        body = f"""
                Hello there!

                I come in peace, this is a test. If you are reading this, it means I have gained the ability to automatically send emails (with attachments) to recipients in various domains from the level of Python code.

                Best Regards,
                main.py
                """
        
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = recipient
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))

        file = open('data.csv', 'rb')
        # Encode as base 64
        attachment = MIMEBase('application', 'octet-stream')
        attachment.set_payload((file).read())
        encoders.encode_base64(attachment)
        attachment.add_header('Content-Disposition', 'attachment; filename= data.csv')
        msg.attach(attachment)

        text = msg.as_string()

        try:
            print('Connecting to server...')
            # Create a connection with smtplib
            server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
            server.starttls()
            server.login(EMAIL_ADDRESS, PASSWORD)
            print('Connection established!')
            print(f'Sending email to {recipient}')
            server.sendmail(EMAIL_ADDRESS, recipient, text)
            print('Email successfully sent!')
        except Exception as e:
            print(e)

    server.quit() # Close the thing once done

send_email()

# try:
#     print('Connecting to server...')
#     # Create a connection with smtplib
#     server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
#     server.starttls(context=simple_email_context)
#     server.login(EMAIL_ADDRESS, PASSWORD)
#     print('Connection established!')
#     print(f'Sending email to {recipient}')
#     server.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, message)
#     print('Email successfully sent!')
# except Exception as e:
#     print(e)
# finally:
#     server.quit() # Close the thing once done
