from django.contrib import admin
# import all models/classes:
from .models import *


# Register your models here.
admin.site.register(Student)
admin.site.register(Portfolio)
admin.site.register(Project)
admin.site.register(ProjectsInPortfolio)