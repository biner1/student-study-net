from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import UserRegisteratoinForm, ProfileUpdateForm


@login_required(login_url='/accounts/login/')
def profile(request):
    if request.method == "POST":
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if p_form.is_valid():
            p_form.save()
            print(p_form)
            messages.success(request,'Profile picture updated successfully')
            return redirect('users:profile')
    else:
        p_form = ProfileUpdateForm
    return render(request,"users/profile.html",{'p_form':p_form}) 


# TODO: if not is super user return 404 response
@login_required(login_url='/accounts/login/')
def register(request):
    if request.user.is_superuser:

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
        
    else:
        return redirect('lectures:home')
    