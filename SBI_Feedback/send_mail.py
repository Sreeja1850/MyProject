import smtplib
from email.mime.text import MIMEText
# from flask.scaffold import _matching_loader_thinks_module_is_packages

def sendemail(customer, rep, rating, comments):
    sender_email = 'sreejaa694@gmail.com'
    rec_email = 'sreejaa694@gmail.com'
    msg = f'<h3>New Feedback Submission</h3><ul><li>Customer: {customer}</li><li>Representative: {rep}</li><li>Rating: {rating}</li><li>Comments: {comments}</li></ul>'
    message = MIMEText(msg, 'html')
    message['Subject'] = 'SBI Feedback'
    message['From'] = sender_email
    message['To'] = rec_email

    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(sender_email, "Abc@123456")
    server.sendmail(sender_email,rec_email,message.as_string())