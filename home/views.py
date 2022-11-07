import datetime
from django.shortcuts import render
import requests
# Create your views here.
def home(request):
    citynew=request.GET.get("cityname","karachi")
    
    url=f'https://api.openweathermap.org/data/2.5/weather?q={citynew}&appid=356b57146de456e5809fa48e947bd426'
    data = requests.get(url).json()
   
    payload={'city':data['name'],
             'weather':data['weather'][0]['main'],
             'icon': data['weather'][0]['icon'],
             'tempeature':data['main']['temp'],
             'temp':"{:.2f}".format(data['main']['temp']-273),
             'humadity':data['main']['humidity'],
             'country':data['sys']['country'],
             'speed':data['wind']['speed'],
             }  
    
    context={'data':payload}
    return render(request,'home.html',context)
