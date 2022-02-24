from django.shortcuts import render

# Create your views here.

def index(request):
    
    return render(request,'basic_app/index.html')

def other(request):
    return render(request,'basic_app/other.html')

def child(request):
    CONTEXT_DICT = {'text':'HELLO WORLD','number':100}
    return render(request,'basic_app/child.html', CONTEXT_DICT)

def relative(request):
    return render(request,'basic_app/relative_url.html')
