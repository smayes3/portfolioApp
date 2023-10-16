from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.views import generic
#from .forms import ProjectForm, PortfolioForm
from django.contrib import messages

# Create your views here.
def index(request):
    #return HttpResponse('home page')
    return render(request, 'portfolio_app/index.html')