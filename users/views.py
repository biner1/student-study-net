from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import UserRegisteratoinForm

@login_required
def register(request):
    if request.method == 'POST':
        form = UserRegisteratoinForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'Acounted created for {username}')
            return redirect('users:register')
    else:
        form = UserRegisteratoinForm
    return render(request, 'users/register.html',{'form':form})