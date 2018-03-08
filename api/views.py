from django.shortcuts import render
from .models import Person, AppStopsModel
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import AppStopsSerializer

# rest framework for post request
from rest_framework.decorators import api_view
from rest_framework.decorators import parser_classes
from rest_framework.parsers import JSONParser

from urllib.request import urlopen
import json as simplejson
import codecs

# Create your views here.

def apina(request):
	
    template = "api/api-view.html"
    context = {'meno' : 'ahoj'}

#    for p in Person.objects.raw('SELECT * FROM app_users'):
#        print(p.username)

    return render(request, template, {'meno': 'ahoj'})

class AppStopsList(APIView):

    def get(self, request):
        stops = AppStopsModel.objects.all()
        serializer = AppStopsSerializer(stops, many=True)
        return Response(serializer.data)

    # @csrf_protect
    @parser_classes((JSONParser,))
    def post(self, request, format=None):

        # print(request.data)
        # print("id:", request.data["id"])
        # print("latitude:", request.data["latitude"])
        # print("longitude:", request.data["longitude"])

        

        app_stops = AppStopsModel()
        
        
        app_stops.latitude = request.data["latitude"]
        app_stops.longitude = request.data["longitude"]
        app_stops.user_id = request.data["user_id"]
        

        response = urlopen("https://maps.googleapis.com/maps/api/geocode/json?latlng="+str(app_stops.latitude)+","+str(app_stops.longitude)+"&key=AIzaSyA4mDvyVrLGN7IkOJw0ks1QACMVrZ1SQ3I")
        reader = codecs.getreader("utf-8")
        data = simplejson.load(reader(response))

        formated_address = data['results'][0]["formatted_address"]
        formated_name = formated_address.split(' ')

        app_stops.name = formated_name[0]
        app_stops.address = formated_address
        app_stops.save()


        return Response({'received data': request.data})
