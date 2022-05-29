from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.main,name = 'main'),
    path('search/', views.search_results, name='search_results'),
    path('imagedetails/<int:galleria_id>', views.one_image, name='imagedetails'),
    # path('location/', views.photo_location, name='photo_location'),
    
    
] 

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)