from django.shortcuts import render
from . import forms

# Create your views here.
def index(request):
    return render(request,'basicapp/index.html')



def form_name_view(request):
    # Initializing the form element
    form = forms.FormName()

    # Checking ig the method is POST
    if request.method == 'POST':
        form = forms.FormName(request.POST)
        # Checking if the form is valid
        if form.is_valid():
            # Do Something Code
            print('Validation Success')
            print("Name -> "+form.cleaned_data['name'])
            print("Email -> "+form.cleaned_data['email'])
            print("Text -> "+form.cleaned_data['text'])

    # returning the form to render in the html
    return render(request,'basicapp/form_page.html',{'form':form})

