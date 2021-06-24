from django.shortcuts import render

from django.http import HttpResponse
from time import sleep
import urllib.request as urllib2
import requests
import random


def index(request):
    readapikey="P6VEWRQC01R7RKTZ"
    channel_id=1355867
    baseURL1= 'https://api.thingspeak.com/channels/1346941/fields/'
    baseURL2='/last.json'
    parameters=[]
    data={}
    try:
        t= 1        
        while t<=5:
            if t>=3:
                baseURL1= 'https://api.thingspeak.com/channels/1355867/fields/'
                baseURL2='/last.json?api_key=P6VEWRQC01R7RKTZ'
            
            get_data= requests.get(baseURL1+str(t)+baseURL2).json()
            parameters.append(get_data['field'+str(t)])
            t+=1
        print(' '.join(parameters))
        pm= random.randint(75,175)
        score=0
        if float(parameters[3])<45 and float(parameters[3])>25: score+=1
        if float(parameters[2])<55:  score+=1
        if float(parameters[4])==0: score+=1
        if float(parameters[1])<600: score+=1
        if pm<125: score+=1
        # data for variable list_of_data
        if score<=1: msg="It is extremely unsafe to go outside!!"
        if score==2: msg="It is unsafe"
        if score==3: msg="Not recommended to go outside!"
        if score==4: msg="Moderately safe"
        if score>=5: msg="It's safe to go outside. Enjoy your day!!"
        data = {
        "O2": parameters[0]+' ppm',
        "CO2":parameters[1]+' ppm',
        "temp": parameters[3] + ' ° C',            
        "humidity": parameters[2] + '%' ,
        "rain": parameters[4],
        "score":str(score),
        "msg":msg,
        "pm":pm
        }
        print(data)
    except:
        print("Error")

    return render(request, "main/index.html", data)