from unittest import result
from django.db import models
import datetime as dt
from cloudinary.models import CloudinaryField

# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length =30)
    def __str__(self):
        return self.category
    def save_category(self):
        self.save()
    def delete_category(self):
        self.delete()
        


class Location(models.Model):
    location = models.CharField(max_length =30)
    def __str__(self):
        return self.location
    def save_location(self):
        self.save()
    def delete_location(self):
        self.delete()


class Galleria(models.Model):
    title = models.CharField(max_length=60)
    image = CloudinaryField('image', null = True)
    # image = models.ImageField(upload_to = 'image/', null=True)
    description = models.TextField()
    location = models.ManyToManyField('location')
    category = models.ManyToManyField('category')
    pub_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

    def save_galleria(self):
        self.save()
    def delete_galleria(self):
        self.delete()
        
    @classmethod
    def days_post(cls):
        today = dt.date.today()
        post = cls.objects.filter(pub_date__date = today)
        return post
    
    
    @classmethod
    def search_by_category(cls, category_term=None):
        result = None
        if category_term is not None:
            result= cls.objects.filter(category__category__icontains=category_term)
            if result.exists():
                return result
        if category_term is not None:
            result = cls.objects.filter(location__location__icontains= category_term)
            if result.exists():
                return result  
        return result
    
   
   
