from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Webpage,AccessRecord,Topic

# Create your views here.
def hello(request):
    return HttpResponse("Hello World!")

def index(request):
    acc_records = AccessRecord.objects.order_by('date')
    my_Dict = {'insert_me':'Hello this is from first_app views.py', 'access_records':acc_records}
    return render(request, 'first_app/index.html', context = my_Dict)
    # return HttpResponse("Hello World!")
