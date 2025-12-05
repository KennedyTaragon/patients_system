from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Patient
from .forms import PatientForm

def add_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Patient added successfully!')
            return redirect('add_patient')
    else:
        form = PatientForm()
    return render(request, 'patients/add_patient.html', {'form': form})

def list_patients(request):
    patients = Patient.objects.all()
    return render(request, 'patients/list.html', {'patients': patients})
