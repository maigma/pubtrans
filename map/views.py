from django.shortcuts import render

# Create your views here.

def maps(request):
	
    template = "map/map-view.html"
    context = {}
    return render(request, template, context)
