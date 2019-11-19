from django.shortcuts import render
from .models import MedEquipment
from django.http import HttpResponse
from .forms import MedForm

def index(request):
    context = {'Med_equipments':MedEquipment.objects.all()}
    EquipmentList = MedEquipment.objects.order_by('-pub_date')[:8]
    return render(request, 'medicalworld/index.html',context)
    
def Med(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = MedForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponse("Thanks for choosing equipment and amount.")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = MedForm()
    return render(request, 'medicalworld/Med.html', {'form': form})