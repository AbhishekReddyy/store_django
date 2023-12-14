from django.shortcuts import render
from django.http import HttpResponse

def cal():
    x = 1
    y = 2
    return x+y
# Create your views here.
def say_hello(request):
    # return HttpResponse("Hello World")
    x = cal()
    return render(request, 'hello.html')