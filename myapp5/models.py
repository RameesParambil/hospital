from django.db import models

# Create your models here.
class Departments(models.Model):
    Dep_name = models.CharField(max_length=100)
    Dep_description = models.TextField()

    def __str__(self):
        return self.Dep_name

class Doctors(models.Model):
    Doc_name = models.CharField(max_length=255)
    Doc_spec = models.CharField(max_length=255)
    Dep_name = models.ForeignKey(Departments, on_delete=models.CASCADE)
    Doc_image = models.ImageField(upload_to='static/doctors_images/')
    
    def __str__(self):
        return self.Doc_name

class Booking(models.Model):
    P_name = models.CharField(max_length=255)
    P_phone = models.CharField(max_length=10)
    P_email = models.EmailField()
    Doc_name = models.ForeignKey(Doctors, on_delete=models.CASCADE)
    Booking_date = models.DateField()
    Booked_on = models.DateField(auto_now=True)

class Add_Patients(models.Model):
    Patient_name = models.CharField(max_length=255)
    Phone = models.CharField(max_length=10)
    Gender = models.CharField(max_length=15)
    Age = models.IntegerField()
    Age_category = models.CharField(max_length=50)