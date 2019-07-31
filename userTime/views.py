from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import user_form,UserTime

# Create your views here.

def timeview(request):
    if request.method=="POST":
        form=user_form(request.POST)
        user=request.POST["username"]

        userTime=UserTime(username=user)
        userTime.save()
        if form.is_valid():
            messages.success(request,'Time Uploaded')
            form.save()

            return  redirect('/appointment/')
    else:
        form=user_form()
    return render(request,'appointment.html',{'form':form})