from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    #return HttpResponse('home page')
    return render(request, 'portfolio_app/index.html')