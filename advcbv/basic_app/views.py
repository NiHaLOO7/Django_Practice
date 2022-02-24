from django.shortcuts import render

# for class based view
from django.views.generic import (View, TemplateView, 
                                ListView, DetailView, 
                                CreateView, UpdateView, 
                                DeleteView)
from django.urls import reverse_lazy
from django.http import HttpResponse
from .  import models

# Create your views here.
# def index(request):
#     return render(request,'index.py')

class CBView(View):
    def get(self,request):
        return HttpResponse("Class Based Views Are Cool!")

class IndexView(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['inject_me'] = 'BASIC INJECTION!'
        return context


# Generic View

"""ListView makes the context dictionary itself and returns it so we do not have to do it externally
    in this case the context dict is school_list (lowercases models.Whatever and appends _list at the
    end so the name would be 'whatever_list') we can change the name using 'context_object_name = name' """

class SchoolListView(ListView):
    context_object_name = 'schools'
    model = models.School
    template_name = 'basic_app/school_list.html'
    # name changed from default school_list to schools
    


"""DetailView just return lowercase of models.Whatever.. whatever would be the name"""

class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    model = models.School
    template_name = 'basic_app/school_detail.html'
    # name changed from default school to school_detail


#it wants a default template of name school_form
class SchoolCreateView(CreateView):
    fields = ('name', 'principle', 'location')
    model = models.School


class SchoolUpdateView(UpdateView):
    fields = ('name', 'principle')
    model = models.School


class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy('basic_app:list')


