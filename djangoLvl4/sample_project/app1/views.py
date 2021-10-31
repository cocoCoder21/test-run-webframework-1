from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    my_dict = {'text':'hello World', 'number': 100}
    return render(request,'app1/index.html',context = my_dict)

def base(request):
    return render(request,'app1/base.html', context={'ewan':''})

def other(request):
    return render(request,'app1/other.html', context={'ewan':''})

def relative(request):
    return render(request,'app1/app1.html', context={'ewan':''})
