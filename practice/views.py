from django.shortcuts import render,redirect
from .forms import homeform
from .models import home

# Create your views here.


def homeviews(request):
    if request.method=="POST":
        form=homeform(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/homeviews/")
        else:
            form=homeform(request.POST)

    else:
        form = homeform(request.POST)
    con={'form':form}
    return  render(request,"home1.html",con)