from django.shortcuts import render
import urllib.request
import json
import folium


# Create your views here.
def index(request):
    if request.method == 'POST':
        city=request.POST['city']
        request_to_url= urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=64ced46d8a03f7fa03f74f14775499ce').read()
        json_data=json.loads(request_to_url) #data received after passing data to url        
        data={
            "country_code": str(json_data['sys']['country']),
            "coordinate":str(json_data['coord']['lon'])+ ' '+ str(json_data['coord']['lat']),
            "temp": str(json_data['main']['temp']) + 'K',
            "pressure": str(json_data['main']['pressure']),
            "humidity": str(json_data['main']['humidity']),
        }
        # Create map object
        m=folium.Map(location=[])

        m=folium.Map()
        m=m._repr_html_()

    else:
        city=''
        data={}
    return render(request, 'index.html', {'city': city,'data': data, 'm': m})