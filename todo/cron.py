# myapp/crons.py
from datetime import timedelta, date

from django_cron import CronJobBase, Schedule
from django.core.mail import send_mail
from Todo_schedular import settings
from .models import *


class MyCronJob(CronJobBase):
    RUN_EVERY_MINS = 1  # Run every 15 minutes
    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'todo.cron.MyCronJob'  # Unique identifier for the cron job

    def do(self):

        print("hii")
        current_date = date.today()
        result_date = current_date + timedelta(days=2)
        mailfrom = settings.EMAIL_HOST_USER
        subject = f"ToDo reminder"
        message = f"Your due date is getting near, and your task is still pending; you should be responsible for your task. "
        user_id_wise_todo_mapping = {}
        todos = Todo.objects.filter(due_date__lte=result_date)
        for todo in todos:
            if user_id_wise_todo_mapping.get(todo.user.email):
                user_id_wise_todo_mapping[todo.user.email].append(todo)
            else:
                user_id_wise_todo_mapping[todo.user.email] = [todo]

        print(user_id_wise_todo_mapping)

        for key, val in user_id_wise_todo_mapping.items():
            for i in val:
                message += "" +i.description
            send_mail(subject, message, mailfrom, [key], fail_silently=False)
            message = f"Your due date is getting near, and your task is still pending; you should be responsible for your task. "
