from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.conf import settings
from . import models


@receiver(post_save,sender=settings.AUTH_USER_MODEL)
def create_student_handler(sender, instance, created, **kwargs):
    if not created:
        return

    student = models.Student(user=instance)
    student.save()
