from django.shortcuts import render
from .models import Person, AppStopsModel
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import AppStopsSerializer

# rest framework for post request
from rest_framework.decorators import api_view
from rest_framework.decorators import parser_classes
from rest_framework.parsers import JSONParser

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


        print(request.data)
        print("id:", request.data["id"])
        print("latitude:", request.data["latitude"])
        print("longitude:", request.data["longitude"])

        return Response({'received data': request.data})
