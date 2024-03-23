from celery import shared_task
from django.conf import settings
from time import sleep
from email.mime.text import MIMEText
import smtplib
@shared_task
def sendemail(email_address):    
    sleep(5)
    print("i am sending")
    me=settings.EMAIL_USERNAME
    password=settings.EMAIL_PASSWORD
    you=email_address
    email_body="""
     <html><body><p>hello user!</p></body></html>
     """
    message=MIMEText(email_body,"html")
    message['Subject']='New Mail'
    message['From']=me
    message['To']=you
    try:
        server=smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(me,password)
        server.sendmail(me,you,message.as_string())
        server.quit()
    except Exception as e:
        print(f'Eroro whil sending email{e}')
