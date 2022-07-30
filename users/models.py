from django.db import models
from django.contrib.auth.models import AbstractUser

from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

from lectures.models import StudentStage


CHOICES=(
    ("uploader","uploader"), 
    ("student","student"),

)


class CustomUser(AbstractUser):
    stage = models.ForeignKey(StudentStage, on_delete=models.CASCADE,blank=False,null=True)
    permissions = models.CharField(max_length=12,choices=CHOICES,blank=False,null=True)


class Profile(models.Model):
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    image =  ProcessedImageField(upload_to='avatars',
                                           processors=[ResizeToFill(300, 300)],
                                           format='JPEG',
                                           options={'quality': 60},default='avatars/default.jpg')

    def __str__(self):
        return f'{self.user.username} Profile'
    