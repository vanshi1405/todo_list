# myapp/crons.py
from datetime import timedelta, date

from django_cron import CronJobBase, Schedule
from django.core.mail import send_mail
from Todo_schedular import settings
from .models import *

# class MyCronJob(CronJobBase):
#     # Schedule the cron job to run daily at midnight (0:00)
#     # RUN_AT_TIMES = ['15:55']
#
#     # The function to be executed by the cron job
def MyCronJob():
    # print("hii")
    current_date = date.today()
    result_date = current_date + timedelta(days=2)
    mailfrom = settings.EMAIL_HOST_USER
    mailto = []
    todos = Todo.objects.filter(due_date__lte=result_date)
    for todo in todos:
        subject = todo.title
        message = todo.description
        mailto.append(todo.user.email)
        send_mail(subject, message, mailfrom, mailto, fail_silently=False)
