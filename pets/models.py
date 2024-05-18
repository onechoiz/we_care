from django.db import models
from django.utils import timezone

class Pet(models.Model):
    ADOPTION_STATUS_CHOICES = [
        ('available', 'Available'),
        ('pending', 'Pending'),
        ('adopted', 'Adopted')
    ]
    
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=50)
    breed = models.CharField(max_length=100, blank=True)
    age = models.IntegerField()
    sex = models.CharField(max_length=10)
    size = models.CharField(max_length=20)
    color = models.CharField(max_length=50)
    health_issues = models.TextField(max_length=200)
    description = models.TextField(max_length=1000)
    adoption_status = models.CharField(max_length=20, choices=ADOPTION_STATUS_CHOICES)
    rescue_organization = models.CharField(max_length=80)
    date_added = models.DateField(default=timezone.now)
    image = models.ImageField(upload_to='pet_images/', blank=True)
    def __str__(self):
        return f"{self.name}"

class AdoptionFosterApplication(models.Model):
    EMPLOYMENT_CHOICES = [
        ('employed', 'Employed'),
        ('retired', 'Retired'),
        ('unemployed', 'Unemployed'),
        ('student', 'Student')
    ]
    applicant_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    address = models.TextField()
    employment_status = models.CharField(max_length=20, choices=EMPLOYMENT_CHOICES)
    other_household_pets = models.TextField()
    is_married = models.BooleanField(default=False)
    children = models.BooleanField(default=False)
    children_description = models.TextField()
    pet_of_interest = models.ForeignKey(Pet, on_delete=models.CASCADE)
    application_status = models.CharField(max_length=20)

class VolunteerApplication(models.Model):
    AVAILABILITY_CHOICES = [
        ('full_time', 'Full Time'),
        ('part_time', 'Part Time'),
        ('weekends', 'Weekends Only'),
        ('evenings', 'Evenings Only')
    ]
    APPLICATION_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected')
    ]
    applicant_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    address = models.TextField()
    availability = models.CharField(max_length=20, choices=AVAILABILITY_CHOICES)
    relevant_experience = models.TextField()
    reason_for_volunteering = models.TextField()
    skills = models.TextField()
    application_status = models.CharField(max_length=20, choices=APPLICATION_STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class About(models.Model):
     heading = models.CharField(max_length=20)
     body  =  models.TextField(max_length=1000)
     
     def __str__(self):
         return self.heading
    
    