from django.contrib import admin


from pictures.models import Galleria, Location, Category


# Register your models here.


@admin.register(Galleria)
class GalleriaAdmin(admin.ModelAdmin):
     filter_horizontal =('location','category')


admin.site.register(Location)
admin.site.register(Category)
