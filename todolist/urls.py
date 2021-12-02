from django.urls import path
from . import views

app_name='todolist'
urlpatterns = [
    path('',views.toDoList,name='toDoList'),
    path('<int:pk>/',views.viewToDo,name='viewToDo'),
    path('toggledone/<int:pk>',views.toggleDone,name='toggleDone'),
    path('deletetask/<int:pk>',views.deleteTask,name="deleteTask"),
    path('addtask/<int:pk>',views.addTask,name="addTask"),
    path('deletelist/<int:pk>',views.deleteTodoList,name="deleteToDoList"),
]