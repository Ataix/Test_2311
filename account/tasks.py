from celery import shared_task
from django.core.mail import send_mail

from Test_2311 import settings


@shared_task()
def send_welcome_email_task(username, email):
    """
    Celery task for sending welcoming email.
    :param username:
    :param email:
    :return:
    """
    subject = 'Successful registration!'
    body = f'Welcome {username}!'
    from_email = settings.EMAIL_HOST_USER
    recipients = [email]
    send_mail(
        subject=subject, message=body, from_email=from_email,
        recipient_list=recipients, fail_silently=False
    )
