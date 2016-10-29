from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'), #goes to the index page
]

# Create your views here.
