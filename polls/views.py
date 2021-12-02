from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .models import LectureVote

from lectures.models import Lectures
from polls.models import LectureVote


@login_required(login_url='/accounts/login/')
def vote(request):
    user=request.user
    if user.is_superuser: # super_user can see all lectures for voting
        lects = Lectures.objects.all()
    else: # Students can vote for lectures of their stage
        lects = Lectures.objects.filter(stage=user.stage)
    has_voted = LectureVote.objects.filter(user=user).exists()
    
    return render(request, 'polls/vote.html', {'lectures':lects,'hasvoted':has_voted})


# TODO: change Vote Count logic for more accurate counting
    # if User has voted and was Deleted vote should be decremented
    # maybe use signals to update vote count
@login_required(login_url='/accounts/login/')
def updateVote(request,lecture): # voting endpoint
    lect = get_object_or_404(Lectures,name=lecture)
    lects = Lectures.objects.all()

    try:
        user = request.user
        has_voted = LectureVote.objects.filter(user=user).exists()
    # TODO: fixing this try, except logic to if else
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

@login_required(login_url='/accounts/login/')
def detail(request):  # show vote detail
    if request.user.is_superuser: # super_user can see all lectures for voting
        lects = Lectures.objects.all()
    else: # Students can vote for lectures of their stage
        lects = Lectures.objects.filter(stage=request.user.stage)
    return render(request,'polls/vote-details.html',{'lectures':lects})