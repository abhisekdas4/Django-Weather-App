from django.shortcuts import render
import urllib.request
import json

def index(request):
    template = 'weatherApp/index.html'
    if request.method == 'POST':
        city = request.POST['city']
        API = 'a4a4456570e232a4b4d1303eebe3ffd9'
        source = urllib.request.urlopen(f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&appid={API}').read()
        list_of_data = json.loads(source)
        data = {
                "country_code": str(list_of_data['sys']['country']),
                "temp" : str(list_of_data['main']['temp']) + '°C',
                "pressure" : str(list_of_data['main']['pressure']),
                "humidity": str(list_of_data['main']['humidity']),
                "main": str(list_of_data['weather'][0]['main']),
                "description":str(list_of_data['weather'][0]['description']),
                "icon": str(list_of_data['weather'][0]['icon']),
                }
        print(data)
    else:
        data = {}

    return render(request, template, data)
