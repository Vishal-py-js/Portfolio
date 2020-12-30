from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'Myprofile/home.html')


def projects(request):
    return render(request, 'Myprofile/projects.html')