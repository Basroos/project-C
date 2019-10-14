from django.shortcuts import render, get_object_or_404

# Create your views here.

from .models import Farmer

def profile_index(request):
   farmers = Farmer.objects.all()
   context={
      'farmers': farmers
   }
   return render(request, "profile.html", context)


# CRUD
# Create retrieve update and delete

