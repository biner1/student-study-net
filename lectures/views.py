from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import *
from .forms import LessonsForm


def home(request):
    stages=StudentStage.objects.all()
    return render(request, 'lectures/home.html',{'stages':stages})

    
def lectures(request,stage):
    try:
        lect=StudentStage.objects.get(stage=stage).lectures_set.all()
    except StudentStage.DoesNotExist:
        raise Http404("Page not found")
    return render(request,'lectures/lectures.html',{'stage':stage,'lectures':lect})


def lessons(request,stage,les):
    try:
        lessons=StudentStage.objects.get(stage=stage).lectures_set.get(name=les).lessons_set.all()
    except Lectures.DoesNotExist:
        raise Http404("Page not found")
    except StudentStage.DoesNotExist:
        raise Http404("Page not found")
    return render(request, 'lectures/lessons.html',{'lessons':lessons,'lecture':les})


@login_required(login_url='/lectures/')
def uploadLecture(request):
    if request.method == 'POST':
        form = LessonsForm(request.POST,request.FILES,user=request.user)
        if form.is_valid():
            form.save()
            return redirect('lectures:home')
    else:
        form = LessonsForm(user=request.user)
    return render(request,'lectures/upload.html',{'form': form})
