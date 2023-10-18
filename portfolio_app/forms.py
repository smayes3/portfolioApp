from django.forms import ModelForm
from .models import *

#create class for project form - ge05
class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields =('title', 'description')


#create class for portfolio form - ge05
class PortfolioForm(ModelForm):
    class Meta:
        model = Portfolio
        #include all fields
        fields = '__all__'