from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *



def index(request):
    title = "Select Location"
    country = Country.objects.all()
    d = {'country': country}
    if request.method == "POST":
        name = request.POST['name']
        country = request.POST['country']
        state = request.POST['states']
        city = request.POST['cities']
        district = request.POST['districts']
        obj = UserResponses.objects.create(name=name,country=Country.objects.get(id=country).name,state=State.objects.get(id=state).name,city=City.objects.get(id=city).name,district=District.objects.get(id=district).name)
        messages.success(request, 'submitted successfully.')
    return render(request,'index.html',d)

def load_states(request):
    country_id = request.GET.get('country')
    states = State.objects.filter(country_id=country_id).order_by('name')
    return render(request, 'states_dropdown_list_options.html', {'states': states})

def load_districts(request):
    state_id = request.GET.get('state')
    districts = District.objects.filter(state_id=state_id).order_by('name')
    return render(request, 'districts_dropdown_list_options.html', {'districts': districts})

def load_cities(request):
    district_id = request.GET.get('district')
    cities = City.objects.filter(district_id=district_id).order_by('name')
    return render(request, 'cities_dropdown_list_options.html', {'cities': cities})

def form (request):
    title = "Select Location"
    if request.method == "POST":
        name = request.POST['name']
        country = request.POST['country']
        state = request.POST['state']
        city = request.POST['city']
        obj = UserResponses.objects.create(name=name,country=country,state=state,city=city)
        messages.success(request, 'submitted successfully.')
    return render(request,'form2.html')



def printresponse(request):
    responses = UserResponses.objects.all()
    parms = {
        "responses":responses,
    }
    return render(request,'responses.html',parms)