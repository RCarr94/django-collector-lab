# TODO: remove this, for testing only --> model coming later

class Dog: 
    def __init__(self, name, breed, description, age):
        self.name = name
        self.breed = breed
        self.description = description
        self.age = age

dogs = [
    Dog('Luna', 'Shepherd', 'smart, friendly, cuddly', 2),
    Dog('Nova', 'Retriever-Mix', 'shy, cuddly, playful', 1),
]


from django.shortcuts import render

from django.http import HttpResponse

# Home View
def home(request):
    return render(request, 'dogs/index.html', { 'dogs': dogs })

def about(request):
    return render(request, 'about.html')

def dogs_index(request):
    return render(request, 'dogs/index.html', { 'dogs': dogs })