from django.contrib import admin


from pictures.models import Galleria, Location, Category


# Register your models here.

admin.site.register(Galleria)
admin.site.register(Location)
admin.site.register(Category)
