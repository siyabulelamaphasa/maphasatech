from django.shortcuts import render

def homepage(request):
    return render(request, 'home/index.html')

def about(request):
    return render(request, 'home/about.html')

def services(request):
    return render(request, 'home/services.html')

def contact(request):
    return render(request, 'home/contact.html')

