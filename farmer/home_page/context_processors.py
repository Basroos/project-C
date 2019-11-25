from farmer_page.models import Farmer
def context_variable(request):
    # .values_list('name', flat=True)
    return {"farmer": Farmer.objects.filter()}
