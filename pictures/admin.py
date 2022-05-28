from django.contrib import admin


from pictures.models import Galleria
from .models import Location


admin.site.register(Galleria)
admin.site.register(Location)


# Register your models here.
