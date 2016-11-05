from django.shortcuts import render

def index(request):
    return render(request, 'personal/home.html')    #render looks in a template folder

def contact(request):
    return render(request, 'personal/basic.html', {'content': ['If you would like to contact me, email me at anthony.shalagin@gmail.com'] } )

# Create your views here.
