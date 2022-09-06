from django.shortcuts import render

# Create your views here.
def base2(request):
    return render(request,'pages/base2.html')
def index(request):
    return render(request,'pages/index.html')