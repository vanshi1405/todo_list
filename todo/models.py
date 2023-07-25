from datetime import datetime
import datetime

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from todo.apps import TodoConfig
priority = [
    ("High", "High"),
    ("Medium", "Medium"),
    ("Low", "Low"), ]
status = [
    ("ToDo", "ToDo"),
    ("Done", "Done"),
    ("Doing", "Doing"), ]


def validate_mobile_number(value):
    mobile_number_str = str(value)
    if len(mobile_number_str) != 10:
        raise models.ValidationError("mobile number contains 10 digit ")
    return value


def present_or_future_date(value):
    if value < datetime.date.today():
        raise models.ValidationError("The date cannot be in the past!")
    return value


#
# class User(User):
#     mobile_number = models.PositiveBigIntegerField(validators=[validate_mobile_number])


class Todo(models.Model):
    user = models.ForeignKey(User, related_name='todo', on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=500)
    due_date = models.DateField(validators=[present_or_future_date])
    status = models.CharField(choices=status, max_length=10)
    priority = models.CharField(choices=priority, max_length=10)
    lable = models.CharField(max_length=10)

    def __str__(self):
        return self.title


# Connect the signal to the Task model

