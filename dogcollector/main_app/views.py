from django.shortcuts import render
from .models import Dog

# Home View
def home(request):
    return render(request, 'dogs/index.html', { 'dogs': dogs })

def about(request):
    return render(request, 'about.html')

def dogs_index(request):
    dogs = Dog.objects.all()
    return render(request, 'dogs/index.html', { 'dogs': dogs })