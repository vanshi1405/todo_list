from datetime import date,timedelta
from time import timezone

from django.apps import AppConfig
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.apps import apps
from django.db.models.signals import post_save
from django.dispatch import receiver
from Todo_schedular import settings

class TodoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'todo'

    # def ready(self):
    #     Todo = apps.get_model('todo', 'Todo')
        #
        # @receiver(post_save, sender= Todo)
        # def send_task_due_email(sender, instance, **kwargs):
        #     # Check if the task is not completed and the due date is within the next 2 days
        #     current_date = date.today()
        #     due_date_threshold = current_date + timedelta(days=2)
        #     if instance.due_date <= due_date_threshold and instance.status in ["ToDo", "Doing"]:
        #         subject = f"Task Due Soon: {instance.title}"
        #         message = f"Dear {instance.user.username},\n\nYour task \"{instance.title}\" is due soon. Please complete it before {instance.due_date}."
        #         from_email = settings.EMAIL_HOST_USER
        #         to_email = [instance.user.email]
        #
        #         send_mail(subject, message, from_email, to_email, fail_silently=False)
        #
        # post_save.connect(send_task_due_email, sender=Todo)