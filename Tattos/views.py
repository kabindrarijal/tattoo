from django.shortcuts import render
from .models import Tatto

# Create your views here.
def tatto_detail(request):
    obj= Tatto.objects.get(id=1)
    context={
        'object':obj
    }
    return render(request,"tattodetail/detail.html",context)


