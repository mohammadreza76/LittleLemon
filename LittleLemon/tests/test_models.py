from django.test import TestCase
from restaurant.models import *


# Create your tests here.

class MenuTest(TestCase):
    
    def test_get_item(self):
        item = Menu.objects.create(title="testtt",price=10,inventory=40)
        item.save()
        itemstr = item.get_item()
   
        self.assertEqual(itemstr,"testtt : 10")
    
