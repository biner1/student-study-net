from django.contrib import admin
from .models import ToDoList, Item


class AdminToDoList(admin.ModelAdmin):
    list_display =("name","user","created")
    list_filter = ("user",)

class AdminItem(admin.ModelAdmin):
    list_display = ("todolist", "text","started")
    list_filter = ("todolist",)

admin.site.register(ToDoList,AdminToDoList)
admin.site.register(Item,AdminItem)