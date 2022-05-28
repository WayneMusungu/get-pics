from django.db import models
import datetime as dt

# Create your models here.
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
    image_pic = models.ImageField(upload_to = 'pics/', null=True)
    description = models.TextField()
    location = models.ManyToManyField('location')
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
