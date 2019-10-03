from django.shortcuts import render

# Create your views here.

def farmer_index(request):
    return render(request, 'farmer_page/farmer.html')