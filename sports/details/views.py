from django.shortcuts import render,redirect
from django.contrib import messages
from .models import ContactSubmission
from .forms import DeliveryForm
from django.http import HttpResponse

def index(request):
    return render(request, 'base/index.html')
def cart(request):
    return render(request, 'base/cart.html')
def contact(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        preference = request.POST.get('preference')
        query_type = request.POST.get('querytype')
        message = request.POST.get('message')

        ContactSubmission.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=phone,
            preference=preference,
            query_type=query_type,
            message=message,
        )

        messages.success(request, 'Your message has been submitted successfully!')
        return redirect('contact')

    return render(request, 'base/contact.html')
def jersey(request):
    return render(request, 'base/jersey.html')
def shoes(request):
    return render(request, 'base/shoes.html')
def accessories(request):
    return render(request, 'base/accessories.html')
def deliveryForm(request):
    if request.method == 'POST':
        form = DeliveryForm(request.POST)
        if form.is_valid():
          
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            company=form.cleaned_data['company'],
            phone=form.cleaned_data['phoneno'],
            address1=form.cleaned_data['address'],
            address2=form.cleaned_data.get('address2', ''),
            address3=form.cleaned_data.get('address3', ''),
            state=form.cleaned_data['state'],
            city=form.cleaned_data['city'],
            postalcode=form.cleaned_data['postalcode'],
            billing_same=form.cleaned_data.get('billing_same', False)
            
            

        
    return render(request, 'base/deliveryForm.html')
def femaleRunningShoes(request):
    return render(request, 'base/femaleRunningShoes.html')
def maleRunningShoes(request):
    return render(request, 'base/maleRunningShoes.html')
def trainingKids(request):
    return render(request, 'base/trainingKids.html')
def trainingmen(request):
    return render(request, 'base/trainingmen.html')
def trainingwomen(request):
    return render(request,'base/trainingwomen.html')
# Create your views here.
