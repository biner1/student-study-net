from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .forms import createNewListForm
from .models import ToDoList, Item


@login_required(login_url='/accounts/login/')
def toDoList(request):
    if request.method=="POST":
        form=createNewListForm(request.POST)
        
        if form.is_valid():
            name=form.cleaned_data['name']
            ToDoList.objects.create(name=name,user=request.user)
            return redirect("todolist:toDoList")
    else:
        form=createNewListForm()
    list=ToDoList.objects.filter(user=request.user)
    return render(request,'todolist/list-todo.html',{"list":list,"form":form})


@login_required(login_url='/accounts/login/')
def viewToDo(request,pk):

    list=get_object_or_404(ToDoList,id=pk,user=request.user)
    
    return render(request,'todolist/view-todo.html',{"list":list})


@login_required(login_url='/accounts/login/')
def toggleDone(request,pk):

    user=request.user
    list=ToDoList.objects.get(id=1,user=user)

    task=get_object_or_404(Item,id=pk)
    
    if task.todolist.user == request.user:
        task.complete=not task.complete
        task.save()
        lsId=task.todolist.id
    else:
        print("task does not exist")
        return redirect('todolist:toDoList')
    return redirect('todolist:viewToDo',pk=lsId)


@login_required(login_url='/accounts/login/')
def addTask(request,pk):

    list=get_object_or_404(ToDoList,user=request.user,id=pk)
    txt = request.POST.get("new")

    if len(txt) > 2 and len(txt) <= 300:
        list.item_set.create(text=txt, complete = False)
    else:
        print("invalid input")
    return redirect('todolist:viewToDo',pk=list.id)


@login_required(login_url='/accounts/login/')
def deleteTask(request,pk):

    task=get_object_or_404(Item,id=pk)
    lsId=task.todolist.id
    task.delete()

    return redirect('todolist:viewToDo',pk=lsId)

@login_required(login_url='/accounts/login/')
def deleteTodoList(request,pk):

    list=get_object_or_404(ToDoList,id=pk,user=request.user)
    list.delete()

    return redirect("todolist:toDoList")