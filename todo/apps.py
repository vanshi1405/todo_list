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
        # # Import your cron job class here to avoid circular imports
        # from .cron import MyCronJob
        #
        # # Register your cron job with the CronJobManager
        # from django_cron import CronJobManager
        # CronJobManager.register(MyCronJob)