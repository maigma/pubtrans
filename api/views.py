from django.shortcuts import render
from .models import Person, AppStopsModel
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import AppStopsSerializer

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

    def post(self):
        pass 
