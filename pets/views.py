from django.shortcuts import render
from django.http import HttpResponse
from . import models

def home(request):
    pets = models.Pet.objects.all()
    # return HttpResponse([ "<li>" + str(pet) + "</li>"  for pet in pets])
    return render(request, "home.html", {"pets": pets})


def contact (request):
    return render(request, "contact.html")

def about(request):
    about = models.About.objects.all()
    return render(request, "about.html", {"about": about} )

def pets(request):
    
    pets = models.Pet.objects.all()
    return render(request, "index.html", {"pets": pets})
    
    
    
def single_pet(request,pet_id):
    pet = models.Pet.objects.get(pk=pet_id)
    return render(request, "single_pet.html", {"pet":  pet})

def donate(request):
     return render(request, "donate.html",)
 
def blog(request):
    blog_posts = models.BlogPost.objects.all()
    return render(request, "blog.html", {"blog": blog_posts})


def adopt_this(request, pet_id):
    pet = models.Pet.objects.get(pk=pet_id)
    return render(request, "adopt.html", {"pet": pet})

def adopt(request):
    return render(request, "adopt.html")