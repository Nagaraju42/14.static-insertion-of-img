from django.shortcuts import render

# Create your views here.
def Flash(request):
    return render(request,'Flash.html')