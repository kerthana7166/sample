from django.shortcuts import render

# Create your views here.
def loadsample(request):
    return render(request,'sample.html')
def loadsample1(request):
    return render(request,'sample1.html')