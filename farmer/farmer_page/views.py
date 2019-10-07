from django.shortcuts import render
from .models import Farmer
# Create your views here.

def farmer_index(request):
    context = {'info': Farmer.objects.all()}
    return render(request, 'farmer_page/farmer.html', context)

def get_farmer(request):
    pass