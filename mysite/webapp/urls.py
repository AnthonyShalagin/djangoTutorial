from django.conf.urls import url
from . import views # . means importing things from the relative package

urlpatterns = [
    url(r'^$', views.index, name = 'index')]    #returns the function from views (index)
