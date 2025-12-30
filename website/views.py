from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

def index_view(request):
    return render(request ,'website/index.html')

def about_view(request):
    return render(request ,'website/about.html')

def contact_view(request):
    return render(request, 'website/contact.html')

def travel_view(request):
    return render(request, 'website/travel.html')

def photography_view(request):
    return render(request, 'website/photography.html')