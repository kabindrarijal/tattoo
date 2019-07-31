from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm

# Create your views here.
def indexView(request):
    return render(request,'home.html')

@login_required

def dashboardView(request):
    return render(request,'dashboard.html')



def registerView(request):
    if request.method=="POST":
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            messages.success(request,'Account created ')
            form.save()
            return  redirect('login_url')
    else:
        form=UserRegisterForm()
    return render(request,'registration/register.html',{'form':form})




