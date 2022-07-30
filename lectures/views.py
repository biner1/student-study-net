from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import Lessons, StudentStage, Lectures
from .forms import LessonsCreateForm, addNewLectureForm, addNewStageForm
from .decorators import can_modify_lesson, superuser_required


def home(request): # stage list
    form = addNewStageForm()
    stages=StudentStage.objects.all()
    return render(request, 'lectures/home.html',{'stages':stages,'form':form})


@login_required(login_url='/accounts/login/')
@superuser_required
def add_stage(request):
    if request.method == 'POST':
        form = addNewStageForm(request.POST)
        if form.is_valid():
            stage = form.cleaned_data['stage']
            StudentStage.objects.create(stage=stage)
            return redirect('lectures:home')
    

def view_lectures(request,stage): # lectures list
    try:
        form = addNewLectureForm()
        lectures=StudentStage.objects.get(stage=stage).lectures_set.all()
    except StudentStage.DoesNotExist:
        raise Http404("Page not found")
    return render(request,'lectures/lectures.html',{'stage':stage,'lectures':lectures,'form':form})


@login_required(login_url='/accounts/login/')
@superuser_required
def add_lectures(request,stage):
     if request.method == 'POST': # add lectures
        form = addNewLectureForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            stage = StudentStage.objects.get(stage=stage)
            Lectures.objects.create(name=name,stage=stage)
            return redirect('lectures:view_lectures', stage)


def lessons(request,stage,les): # lessons list
    try:
        lessons=StudentStage.objects.get(stage=stage).lectures_set.get(name=les).lessons_set.all()
    except Lectures.DoesNotExist:
        raise Http404("Page not found")
    return render(request, 'lectures/lessons.html',{'lessons':lessons,'lecture':les})


@login_required(login_url='/accounts/login/')
@can_modify_lesson
def upload_lecture(request):
    if request.method == 'POST':
        form = LessonsCreateForm(request.POST,request.FILES,user=request.user)
        if form.is_valid():
            form.save()
            return redirect('lectures:home')
    else:
        form = LessonsCreateForm(user=request.user)
    return render(request,'lectures/upload.html',{'form': form})



@login_required(login_url='/accounts/login/')
@superuser_required
def delete_stage(request,stage):
    stage = get_object_or_404(StudentStage,stage=stage)
    stage.delete()
    return redirect('lectures:home')


@login_required(login_url='/accounts/login/')
@superuser_required
def delete_lecture(request,stage,lect):
    stage = get_object_or_404(StudentStage,stage=stage)
    lecture = get_object_or_404(Lectures,stage=stage,name=lect)
    lecture.delete()
    return redirect('lectures:view_lectures', stage)


@login_required(login_url='/accounts/login/')
@can_modify_lesson
def delete_lesson(request,lect,title):
    lect = get_object_or_404(Lectures,name=lect)
    lesson = get_object_or_404(Lessons,title=title,lectures=lect)
    lesson.delete()
    return redirect('lectures:home')