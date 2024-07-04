from sender import send_email


# Your email contents go here
recipients = ['piotr.bledowski.77@gmail.com']
subject = 'Hello!'
body = 'Your automated e-mail is here!'
attachment = 'data.csv'

send_email(recipients=recipients, subject=subject, body=body, attachment=attachment)
