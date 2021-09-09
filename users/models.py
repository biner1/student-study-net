from django.db import models
from django.contrib.auth.models import AbstractUser
from lectures.models import StudentStage

# Create your models here.

class CustomUser(AbstractUser):
    stage = models.ForeignKey(StudentStage, on_delete=models.CASCADE, blank=False, null=True)


