from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import LectureVote

from lectures.models import Lectures
from polls.models import LectureVote

@login_required(login_url='/lectures/')
def vote(request):
    lects = Lectures.objects.all()
    user = request.user
    
    if request.method == 'POST':
        try:
            
            selected=Lectures.objects.get(pk=request.POST['choice'])
            has_voted = LectureVote.objects.filter(user=user).exists()

        except (KeyError, Lectures.DoesNotExist):
            return render(request, 'polls/vote.html', {
            'lectures':lects,
            'error_message': "You didnt selct a choice",
        })
        else:
            if has_voted:
                vLect = LectureVote.objects.get(user=user).lecture
                vote = LectureVote.objects.get(user=user,lecture=vLect)
                vLect.vote_count-=1
                vLect.save()
                vote.delete()
            else:
                vote=LectureVote.objects.create(user=user,lecture=selected)
                selected.vote_count+=1
                selected.save()
                vote.save()
            return redirect('polls:vote')

    else:
        return render(request, 'polls/vote.html', {'lectures':lects})


def detail(request):
    lects = Lectures.objects.all()
    return render(request,'polls/vote-details.html',{'lectures':lects})