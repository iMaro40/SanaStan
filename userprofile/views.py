from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
@login_required(login_url='/login/')
def myprofile(request):
    if request.method == 'POST':
        userForm = UserUpdateForm(request.POST, instance = request.user)
        profileForm = ProfileUpdateForm(request.POST, request.FILES, instance = request.user.profile)
        if userForm.is_valid() and profileForm.is_valid():
            userForm.save()
            profileForm.save()
            messages.success(request, "Your profile was successfully updated!")
            return redirect('profile')
    else:
        userForm = UserUpdateForm(instance = request.user)
        profileForm = ProfileUpdateForm(instance = request.user.profile)

    context = {
        'userForm': userForm,
        'profileForm': profileForm
    }
    return render (request, 'userprofile/profile.html',context)
