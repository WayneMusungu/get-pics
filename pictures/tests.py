from unicodedata import category
from django.test import TestCase
from .models import Category, Location, Galleria

# Create your tests here.

class CategoryTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.culture= Category()
        
     # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.culture,Category))
        
        # Testing Save Method
    def test_save_method(self):
        self.culture.save_category()
        categorys = Category.objects.all()
        self.assertTrue(len(categorys) > 0)
     
class LocationTestClass(TestCase):
    # Setup Method
    def setUp(self):
        self.Kenya= Location()
        
     # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.Kenya,Location))
        
        # Testing Save Method
    def test_save_method(self):
        self.Kenya.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)
    
        
