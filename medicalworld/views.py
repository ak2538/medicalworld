from django.shortcuts import render
from .models import MedEquipment

def index(request):
    context = {'Med_equipments':MedEquipment.objects.all()}
    EquipmentList = MedEquipment.objects.order_by('-pub_date')[:8]
    return render(request, 'medicalworld/index.html',context)
    