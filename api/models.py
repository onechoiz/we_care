from  tastypie.resources  import ModelResource
from  pets  import models

# Create your models here.

class PetResource(ModelResource):
    class Meta:
        queryset = models.Pet.objects.all()
        resource_name =  "pets"
        allowed_metods = ["get","post", "delete", "patch"]


