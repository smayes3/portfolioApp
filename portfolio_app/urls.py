from django.urls import path
from . import views

urlpatterns= [
    #path function defines a url pattern
    #'' is empty to represent based path to app
    # views.index is the function defined in views.py
    # name='index' parameter is to dynamically create url
    # example in html <a href="{% url 'index' %}">Home</a>.
    path('', views.index, name='index'),


    # path function defines: (using students/ path as example)
    # a pattern to match against the URL ('students/'), 
    # a view function that will be called if the URL matches (views.StudentListView.as_view()), 
    # and a name for the mapping
    
    # the URL must already have matched "/portfolio_app", so the view will actually
    # be called for the URL "/portfolio_app/students/"

    # source: https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Generic_views#url_mapping

    #add paths for generic student list and detail views - GE05
    path('students/', views.StudentListView.as_view(), name='students'),
    path('student/<int:pk>', views.StudentDetailView.as_view(), name='student-detail'),


]