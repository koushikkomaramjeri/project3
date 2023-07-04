from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def input(request):
    return render(request,'input.html')
def add(request):
    x=request.POST["t1"]
    y=request.POST["t2"]
    i=int(x)
    j=int(y)
    z=i+j
    res=HttpResponse("The sum is: "+str(z))
    return res