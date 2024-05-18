from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.Pet)
admin.site.register(models.VolunteerApplication)
admin.site.register(models.AdoptionFosterApplication)
admin.site.register(models.About)

# change the name of  the admin panel 

admin.site.site_header = "WeCare Admin Access"
admin.site.site_title = "WeCare Admin"
admin.site.index_title = "Welcome to the WeCare Admin Area"
