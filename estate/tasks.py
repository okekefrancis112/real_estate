from celery import shared_task
from django.core.mail import EmailMultiAlternatives, send_mail
from django.conf import settings
import sys

@shared_task
def send( subject, text_content, from_email, receiver_emails):
    try:
        send_mail(subject, text_content, from_email, receiver_emails)
        print(">>>>>>>>>>>", send_mail)
        
        return True
    except:
        print(sys.exc_info()[0])
        return False