from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_views(request):
    return render(request,"home.html",{})

def contact(request):
    return render(request, "contact.html", {})

def category(request):
    return render(request,"category.html",{})

def about_us(request):
    my_context={
        "title":"this is all about us ",
        "my_html":"<h1> this is html</h1>"
    }
    return render(request,"aboutus.html",my_context)

def appointView(request):
    return render(request, "appointment.html", {})
