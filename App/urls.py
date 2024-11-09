from django.urls import path
from App import views

urlpatterns = [
    path("" ,views.search,name="search"),    
    path("home/",views.home,name="home"),
    path("search/",views.search,name="search"),
    path("about/", views.about, name="about"),

]


