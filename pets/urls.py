from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = "index"),
    path('contact/', views.contact, name = "contact"),
    path('about/', views.about, name = "about"),
    path('blog/', views.blog, name = "blog"),
    path('donate/', views.donate, name = "donate"),
    path('pets/adopt/<int:pet_id>', views.adopt, name = "adopt_this"),
    path('pets/adopt/', views.adopt, name = "adopt"),
    path("pets/", views.index, name = "pets"),
    path("pets/<int:pet_id>/", views.single_pet, name = "single_pet")
]