from django.shortcuts import render
#from .models import Driver
from .forms import DriversForm
# Create your views here.
def Driver(request):
    if request.method == "POST":
        form = DriversForm(request.POST or None)
        if form.is_valid():
            form.save()
        return render(request,"authentication/driver_dashboard.html",{})
    else:
        return render(request,"authentication/index.html",{})

#def driver_dashboard(request):
  #  return render(request,"authentication/driver_dashboard.html")

