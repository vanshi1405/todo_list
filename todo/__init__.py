

default_app_config = 'todo.apps.TodoConfig'
# myapp/__init__.py

from django_cron import CronJobManager


from .cron import MyCronJob
# Register your cron job with the CronJobManager
CronJobManager.register(MyCronJob)
