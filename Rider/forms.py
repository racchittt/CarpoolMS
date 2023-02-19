from django import forms
from Rider.models import Riders

class RidersForm(forms.ModelForm):
    class Meta:
        model = Riders
        fields = ['userId','fname','lname','pickup','user_destination']