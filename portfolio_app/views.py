from django.shortcuts import render
from django.http import HttpResponse

# GE05 updates:
from .models import *   # --> import all models defined in models.py
from django.views import generic 
#from .forms import ProjectForm, PortfolioForm  # --> commented out during GE05 apply models and db prep
from django.contrib import messages

# Create your views here.
def index(request):
    #return HttpResponse('home page')
    return render(request, 'portfolio_app/index.html')


# GE05 - APPLY create generic student list and detail views

#instead of using a regular function like one for index (above), use class-based generic list view (ListView)
#(ListView) class inherits from an existing view

# the generic view will query the db to get all records for the model (student in this example) 
# then render a template located at .../templates/portfolio_app/student_list.html
# within the template, you can access the list of students with the template variable named <modelName>_list

# source: https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Generic_views#view_class-based

#create generic student list view - ge05
class StudentListView(generic.ListView):
    model = Student 

#create generic student detail view - ge05
class StudentDetailView(generic.ListView):
    model = Student
