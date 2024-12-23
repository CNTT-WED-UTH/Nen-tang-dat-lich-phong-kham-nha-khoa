from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class Patient(models.Model):
    user= models.OneToOneField(User, on_delete= models.SET_NULL, null= True, blank= False)
    name= models.CharField(max_length= 200, null= True)
    email= models.CharField(max_length= 200, null= True)
    address= models.CharField(max_length= 200, null= True)
    phonenumber= models.IntegerField(max_length= 200, null= True)
    def __str__(self):
        return self.name

class Dentist(models.Model):
    name= models.CharField(max_length= 200, null= True)
    email= models.CharField(max_length= 200, null= True)
    Specialty= models.CharField(max_length= 200)
    phonenumber= models.IntegerField(max_length= 200, null= True)
    ClinicAddress= models.CharField(max_length= 200)
    def __str__(self):
        return self.name

class Service(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
    
class Appointment(models.Model):
    patients= models.ForeignKey(Patient, on_delete=models.SET_NULL, null= True, blank= True)
    dentists= models.ForeignKey(Dentist, on_delete=models.SET_NULL, null= True, blank= True)
    date_booking= models.DateTimeField(auto_now_add= True)
    complete= models.BooleanField(default= False, null= True, blank= False)
    transaction_id= models.CharField(max_length= 200, null= True)
    note= models.TextField(max_length= 500)
    def __str__(self):
        return str(self.id)