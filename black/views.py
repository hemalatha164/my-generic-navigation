from django.shortcuts import render

# Create your views here.
def rose(request):
    return render(request,'rose.html')