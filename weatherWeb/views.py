from django.shortcuts import render
import json
import urllib.request
# Create your views here.


def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        res = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=625d6bc5ca9eeb0183d922353b11d4f6').read()
        json_data = json.loads(res)
        data = {
            "country_code": str(json_data['sys']['country']),
            "coordinate": str(json_data['coord']['lon'])+' ' +
            str(json_data['coord']['lat']),
            "temp": str(json_data['main']['temp']),
            "pressure": str(json_data['main']['pressure']),
            "humidity": str(json_data['main']['humidity']),
        }
        
        
    else:
        city = ''
        data = {}

    return render(request, 'index.html',{'city':city , 'data':data})
