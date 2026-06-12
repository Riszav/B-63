from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings


@shared_task
def add(x, y):
    print("start adding", x, y)
    from time import sleep

    sleep(15)
    return x + y


@shared_task
def send_otp_mail(email, code):
    send_mail(
        subject="OTP for registration",
        message=f"code: {code}",
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email],
        fail_silently=False,
    )
    return "OK"


@shared_task
def send_report_mail():
    send_mail(
        subject="Отчет о важнах делах",
        message="что то очень важное",
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=["riszav.01@gmail.com"],
        fail_silently=False,
    )
    return "OK"
