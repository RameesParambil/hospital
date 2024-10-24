from django.shortcuts import render, redirect
from django.http import HttpResponse 
from django.contrib import messages
from .models  import Departments,  Doctors, Booking, Add_Patients

# Create your views here.
def home(request):
    
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html') 

def booking_post(request):
    user=Doctors.objects.all()
    if request.method=='POST':
        p_name=request.POST['p_name']
        p_phone=request.POST['p_phone']
        p_email=request.POST['p_email']
        doc_name=request.POST['doc_name']
        booking_date=request.POST['booking_date']
        doctor=Doctors.objects.get(Doc_name=doc_name)
        print(doctor)
        user=Add_Patients.objects.filter(Patient_name=p_name,Phone=p_phone)
        if user:
            print("success")    
            Booking.objects.create(P_name=p_name,P_phone=p_phone,P_email=p_email,Doc_name=doctor,Booking_date=booking_date)
            return redirect('confirmation')
        else:
            print("failed")
            messages.error(request, ' Please enter a valid patient name and registered phone number. ')
            return redirect ('booking')
    return render(request, 'booking.html',{'user':user})

def doctors(request):
    show=Doctors.objects.all()
    return render(request, 'doctors.html', {'show':show})

def contact(request):
    return render(request, 'contact.html')

def department(request):
    user=Departments.objects.all() 
    return render(request, 'department.html',{'user':user})

def confirmation(request):
    return render(request,'confirmation.html')

def add_patient(request):
    if request.method=='POST':
        patient_name=request.POST['patient_name']
        phone=request.POST['phone_number']
        gender=request.POST['gender']
        age=request.POST['patient_age']
        age_category=request.POST['age_category']   
        Add_Patients.objects.create(Patient_name=patient_name,Phone=phone,Gender=gender,Age=age,Age_category=age_category)
        return redirect ('booking')
    return render(request,'new.html')












