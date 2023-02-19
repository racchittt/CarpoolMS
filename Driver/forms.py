from django import forms
from Driver.models import Drivers

class DriversForm(forms.ModelForm):
    class Meta:
        model = Drivers
        fields = ['driverId','driver_fname','driver_lname','starting_destination','destination','car_model','no_of_seats']