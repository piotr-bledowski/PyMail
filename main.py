from sender import send_email


# Your email contents go here
recipients = ['john.doe@example.com', 'jane.doe@yahoo.com']
subject = 'Hello!'
body = 'Your automated e-mail is here!'
attachment = 'data.csv'

send_email(recipients=recipients, subject=subject, body=body, attachment=attachment)
