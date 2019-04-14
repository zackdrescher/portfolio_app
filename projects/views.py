from django.shortcuts import render
from projects.models import Project

def project_index(request):
    """Index page containing all projects"""
    # query all projects 
    projects = Project.objects.all()
    # build the context
    context = {
        'projects': projects
    }
    # render the html with the given context
    return render(request, 'project_index.html', context)
