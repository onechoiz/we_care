from  tastypie.resources  import ModelResource
from  pets  import models
from tastypie.authorization import Authorization
from .auth import CustomAuth

# Create your models here.

class PetResource(ModelResource):
    class Meta:
        queryset = models.Pet.objects.all()
        resource_name =  "pets"
        allowed_metods = ["get", "post", "delete", "patch"]
        authentication = CustomAuth()
        authorization = Authorization()
        # excluding what api can see 
        excludes = ["status"]
        


