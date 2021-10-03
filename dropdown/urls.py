from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('form2/',views.form,name='form'),
    path('load-states/', views.load_states, name='ajax_load_states'),
    path('load-districts/', views.load_districts, name='ajax_load_districts'),
    path('load-cities/', views.load_cities, name='ajax_load_cities'),
    path('responses/',views.printresponse,name='responses'),
]
