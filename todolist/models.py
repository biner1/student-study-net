from django.db import models
from django.conf import settings



class ToDoList(models.Model):
    name=models.CharField(max_length=200)
    user=models.ForeignKey(settings.AUTH_USER_MODEL,null=True,on_delete=models.CASCADE)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Item(models.Model):
    todolist=models.ForeignKey(ToDoList,on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    complete=models.BooleanField(default=False)

    def __str__(self):
        return self.text

    class Meta:
        ordering = ['complete']