from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

# Create your views here.
def index(request):
    #39.64205411653517, 27.88331103782429
    lat=27.88331103782429
    long=39.64205411653517
    kooardinat=f"<iframe src='https://maps.google.com/maps?q={long,lat}&output=embed'  width='830' height='820' style='border:0;' allowfullscreen='' loading='lazy' referrerpolicy='no-referrer-when-downgrade' ></iframe>"
    context={
        'pil':10,
        'hiz':5,
        'mod':"LAND",
        'irtifa':12,
        'heading':12,
        'lat':lat,
        'long':long,
        'kooardinat':kooardinat
    }
    template = loader.get_template('index.html')
    return render(request,'index.html',context)