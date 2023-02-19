#from django.db import translation
from django.db import models

# Create your models here.
class Riders(models.Model):
    userId = models.CharField(max_length = 200 , primary_key=True)
    fname = models.CharField(max_length = 100)
    lname = models.CharField(max_length = 100)
    pickup = models.CharField(max_length = 100)
    user_destination = models.CharField(max_length = 100)
    
    
    def __str__(self):
        return self.userId +" "+self.fname
