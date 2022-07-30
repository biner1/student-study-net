from django.db import models
from lectures.models import Lectures
from users.models import CustomUser

class LectureVote(models.Model):


    lecture = models.ForeignKey(Lectures, on_delete=models.CASCADE,related_name='lecturesv',null=True)
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True,blank=True)
   
    def __str__(self):
        return str(self.user) + ' voted for ' + str(self.lecture)
