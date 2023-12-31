from typing import Any
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse

# GE05 updates:
from .models import *   # --> import all models defined in models.py
from django.views import generic 
#from .forms import ProjectForm, PortfolioForm  # --> commented out during GE05 apply models and db prep
from django.contrib import messages
from portfolio_app.forms import * # --> import all forms defined in forms.py

# Create your views here.

#update in GE05
def index(request):
    student_active_portfolios = Student.objects.select_related('portfolio').all().filter(portfolio__is_active=True)
    print("active portfolio query set", student_active_portfolios)
    return render( request, 'portfolio_app/index.html', {'student_active_portfolios':student_active_portfolios})



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
class StudentDetailView(generic.DetailView):
    model = Student


#create generic Portfolio list view - ge05
class PortfolioListView(generic.ListView):
    model = Portfolio

#create generic Portfolio detail view - ge05
class PortfolioDetailView(generic.DetailView):
    model = Portfolio

    #override get_context_data() function to show all projects in the portfolio - ge05
    #source: 
    # https://docs.djangoproject.com/en/4.2/topics/class-based-views/generic-display/
    # https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Generic_views
    def get_context_data(self, **kwargs):
        
        #call base implementation to get context
        context = super().get_context_data(**kwargs)
        #add QuerySet of all projects
        context["project_list"] = Project.objects.all()
        #return the QS
        return context



#create generic Project list view - ge05
class ProjectListView(generic.ListView):
    model = Project

#create generic Project detail view - ge05
class ProjectDetailView(generic.DetailView):
    model = Project



#create project function - ge05
# creates project associated with a portfolio
# source:
# https://chat.openai.com/share/e5e5d2b2-58ed-4420-ab7c-0e79732a697b
# https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Forms
def createProject(request, portfolio_id):
    #create project form
    form = ProjectForm()
    #get the portfolio based on id/pk
    portfolio = Portfolio.objects.get(pk=portfolio_id)
    
    if request.method == 'POST':
        # Create a new dictionary with form data and portfolio_id
        project_data = request.POST.copy()
        project_data['portfolio_id'] = portfolio_id
        
        #update the form with the data
        form = ProjectForm(project_data)
        
        if form.is_valid():
            # Save the form without committing to the database
            project = form.save(commit=False)
            # Set the portfolio relationship
            project.portfolio = portfolio
            #save project
            project.save()

            # Redirect back to the portfolio detail page
            return redirect('portfolio-detail', portfolio_id)
    
    #update dictionary
    context = {'form': form}

    #render the form
    return render(request, 'portfolio_app/project_form.html', context)


#function to delete project from portfolio detail page - ge05
# pk is project id
# sources:
# https://www.geeksforgeeks.org/delete-view-function-based-views-django/
def deleteProject(request, pk, portfolio_id):
    
    #get the project that needs to be deleted
    project = get_object_or_404(Project, pk=pk)

    #get portfolio id
    portfolioID = Portfolio.objects.get(pk=portfolio_id)

    #set dictionary values
   # projectTitle = Project.objects.get(title=project.title)
    context = {'title': project.title}

    #delete the project
    if request.method == "POST":
        project.delete()

        #redirect back to portfolio detail page
        return redirect('portfolio-detail', portfolio_id)
    
    #display delete confirmation page
    return render(request, "portfolio_app/project_delete.html", context) 


#function to update project from portfolio detail page - ge05
#sources:
# https://www.geeksforgeeks.org/update-view-function-based-views-django/?ref=lbp
def updateProject(request, pk, portfolio_id):
    #initialize dictionary
    context = {}
    #get portfolio and project id
    portfolio = Portfolio.objects.get(pk=portfolio_id)
    project = get_object_or_404(Project, pk=pk)    
    
    #pass project as form instance
    form = ProjectForm(request.POST or None, instance=project)

    #save form data and redirect
    if form.is_valid():
        form.save()
        return redirect('portfolio-detail', portfolio_id)
    
    #add form dictionary to context and render
    context["form"] = form
    return render(request, 'portfolio_app/project_update.html', context)



#function to update portfolio from student details page - ge05
def updatePortfolio(request, pk):
    #initialize dictionary
    context = {}
    #get portfolio id
    portfolio = get_object_or_404(Portfolio, pk=pk)

    #pass portfolio as form instance
    form = PortfolioForm(request.POST or None, instance=portfolio)

    #save form and redirect back to student details
    if form.is_valid():
        form.save()
        return redirect('student-detail', pk)
    
    #add form dictionary to context and render
    context["form"] = form
    return render(request, 'portfolio_app/portfolio_form.html', context)

