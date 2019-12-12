import os
from django.core.mail import send_mail
from django.shortcuts import render
from .models import Farmer
from user_profile.models import Product
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, get_list_or_404, redirect
from farmer_page.models import Farmer
from django.db.models import Q
from user_profile.models import Product
from farmer_page.forms import UpdateUser, ReportForm
from django.contrib import messages
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
# Create your views here.

def farmer_index(request):
    context = {'info': Farmer.objects.all(),
                'navigation':'farmer'}
    return render(request, 'farmer_page/farmer.html', context)

def profile(request, id):
    # Report form and take id
    # Go to the farmer
    farmer = get_object_or_404(Farmer, pk=id)
    context = {'farmer':farmer,
                'prods':Product.objects.all()   
    }
    if request.method == "POST":
        form = ReportForm(request.POST)
        if form.is_valid():
            from_email = form.cleaned_data['from_email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            message = Mail(from_email=from_email, to_emails='Ahmet_karatas@live.nl', subject=subject, html_content=message)
            # send_mail(subject, message, from_email, [
            #           'Ahmet_karatas@live.nl'], fail_silently=False)
            sg = SendGridAPIClient(
                api_key='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')
            response = sg.send(message)
            print(response.status_code)
            messages.success(request, 'REPORTED!')
    form = ReportForm()
    context = {'farmer':farmer, "form":form}
    return render(request, 'farmer_page/profile.html', context)

def my_products(request):
    current_user = request.user.id
    template = 'farmer_page/my_products.html'
    profile = get_object_or_404(User, pk=current_user)
    # products = get_list_or_404(Product, product_user=request.user)
    products = Product.objects.filter(product_user=request.user)

    return render(request, template, {'profile':profile, 'product': products})

def my_profile(request):
    current_user = request.user.id
    template = 'farmer_page/my_profile.html'
    profile = get_object_or_404(Farmer, pk=current_user)
    context = {'profile':profile}
    return render(request, template, context)

def update_profile(request):
    template = 'farmer_page/update_profile.html'
    if request.method == 'POST':
        instance = get_object_or_404(Farmer, pk=request.user.id)
        print(instance)
        update_form = UpdateUser(request.POST, instance=instance)
        print(update_form.errors)
        if update_form.is_valid():
            print("klopt")
            update_form.save()
            # updated_email = update_form.cleaned_data['email']
            # updated_name = update_form.cleaned_data['name']
            # updated_address = update_form.cleaned_data['address']
            # updated_age = update_form.cleaned_data['age']
            # updated_province =update_form.cleaned_data['province']
            # updated_company_name = update_form.cleaned_data['farm']
            # updated_phone_number = update_form.cleaned_data['phone_number']
            # updated_products = update_form.cleaned_data['products']
            # # email toevoegen
            # farmer = Farmer.objects.filter(name=request.user).update(name=updated_name, address=updated_address, age=updated_age, province=updated_province, company_name=updated_company_name, phone_number=updated_phone_number, products=updated_products)
            return redirect('farmer-index')

    else:
        print(request.method)
        update_form = UpdateUser(instance=request.user)
        print("not working ")
    
    return render(request, template, {'updateuser': update_form})

def search_farmer(request):
    template = 'farmer_page/farmer.html'
    query_farmer = request.GET.get("query")
    if query_farmer:
        # result = Farmer.objects.filter(Q(address__icontains=query_farmer) | Q(products__icontains=query_farmer))
        result = Farmer.objects.filter(name__startswith=query_farmer)
        if len(result) < 1:
            empty = True
        else:
            empty = False

    return render(request, template, {'result':result, 'empty':empty})

