from django.forms import ModelForm
from .models import Project

#create class for project form - ge05
class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields =('title', 'description')
