from django.shortcuts import render
from .models import *
app_name = "home"

# Create your views here.

def base():
    view = {}
    view['feedbacks'] = Feedback.objects.all()
    return view

def home(request):
    return render(request, 'index.html', base())

def about(request):
    return render(request, 'about.html', base())

def contact(request):
    if request.method =='POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        data = Contact.objects.create(
            name = name,
            email = email,
            subject = subject,
            message = message
        )
        data.save()
        return render(request, 'contact.html', {"message":"Success"})

    return render(request, 'contact.html')

def portfolio(request):
    return render(request, 'portfolio.html')

def price(request):
    return render(request, 'price.html')

def services(request):
    return render(request, 'services.html', base())