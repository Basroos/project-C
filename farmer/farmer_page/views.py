from django.shortcuts import render
from .models import Farmer
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
# Create your views here.

def farmer_index(request):
    context = {'info': Farmer.objects.all(),
                'navigation':'farmer',}
    return render(request, 'farmer_page/farmer.html', context)


def profile(request, id):
    farmer = get_object_or_404(Farmer, pk=id)
    context = {'farmer':farmer}
    return render(request, 'farmer_page/profile.html', context)
