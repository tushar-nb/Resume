from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def HomeApi(request):
    return render(request,'home.html')

def Success(request):
    return HttpResponse("Success")