from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import LectureVote

from lectures.models import Lectures
from polls.models import LectureVote

@login_required(login_url='/accounts/login/')
def vote(request):
    user=request.user
    lects = Lectures.objects.all()
    has_voted = LectureVote.objects.filter(user=user).exists()
    
    return render(request, 'polls/vote.html', {'lectures':lects,'hasvoted':has_voted})


@login_required(login_url='/accounts/login/')
def updateVote(request,lecture):
    lect = get_object_or_404(Lectures,name=lecture)
    lects = Lectures.objects.all()

    try:
        user = request.user
        has_voted = LectureVote.objects.filter(user=user).exists()

    except (KeyError, Lectures.DoesNotExist):
        return render(request, 'polls/vote.html', {
        'lectures':lects,
        'error_message': "You didnt selct a choice",
    })
    else:
        if has_voted: # if user has voted remove vote
            vLect = LectureVote.objects.get(user=user).lecture
            vote = LectureVote.objects.get(user=user,lecture=vLect)
            vLect.vote_count-=1
            vLect.save()
            vote.delete()
        else:
            vote=LectureVote.objects.create(user=user,lecture=lect)
            lect.vote_count+=1
            lect.save()
            vote.save()
        return redirect('polls:detail')


def detail(request):
    lects = Lectures.objects.all()
    return render(request,'polls/vote-details.html',{'lectures':lects})