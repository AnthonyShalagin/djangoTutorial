from django.shortcuts import render

def index(request):
    return render(request, 'personal/home.html')    #render looks in a template folder


# Create your views here.
