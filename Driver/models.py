from django.db import models

# Create your models here.
class Drivers(models.Model):
    driverId = models.CharField(max_length = 200 , primary_key=True)
    driver_fname = models.CharField(max_length = 100)
    driver_lname = models.CharField(max_length = 100)
    starting_destination = models.CharField(max_length = 200)
    destination = models.CharField(max_length = 200)
    car_model = models.CharField(max_length = 20)
    no_of_seats = models.IntegerField()
    
    def __str__(self):
        return self.driverId +" "+self.driver_name
class Item(models.Model):
    driver= models.ForeignKey(Drivers, on_delete=models.CASCADE)