from django.shortcuts import render
from Rider.forms import RidersForm
from Rider.models import Riders

# Create your views here.
#def user_dash(request):
 #       return render(request,"authentication/user_dashboard.html",{})
     
def Rider(request):
    if request.method == "POST":
        form = RidersForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
        return render(request,"authentication/Rider.html",{})
    else:
        return render(request,"authentication/Rider.html",{})