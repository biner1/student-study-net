from django.db import models
from django.utils.text import slugify


class StudentStage(models.Model):
    stage = models.CharField(max_length=20, null=True)
    
    def __str__(self):
        return self.stage


class Lectures(models.Model):
    name = models.CharField(max_length=200, blank=False)
    stage = models.ForeignKey(StudentStage, on_delete=models.CASCADE , blank=False, null=False)
    vote_count = models.IntegerField(blank=True,null=True,default=0)

    def save(self, *args, **kwargs):
        
        self.name = slugify(self.name)
        super(Lectures, self).save(*args, **kwargs)

        

    def __str__(self):
        return self.name


class Lessons(models.Model):
    title = models.CharField(max_length=200, blank=False, null=False)
    upload = models.FileField(upload_to='uploads/')
    lectures = models.ForeignKey(Lectures,on_delete=models.CASCADE, null=True, blank=False)
    uploaded=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title