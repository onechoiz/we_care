from  tastypie.resources  import ModelResource
from  pets  import models

# Create your models here.

class PetResource(ModelResource):
    class Meta:
        def get_queryset(self):
            queryset = models.Pet.objects.all()
            resource_name =  "pets"
            allowed_metods = ["get","post", "delete", "patch"]

