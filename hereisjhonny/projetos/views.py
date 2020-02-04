from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def projects(request):
    return render(request, "projects.html")

def project(request, project_name):
    return HttpResponse("Esss aqui é o projeto %s" % project_name)

def contat(request):
    return render(request, "contact.html")
